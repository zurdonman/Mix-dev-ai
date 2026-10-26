#!/usr/bin/env python3
"""Sincroniza los repos upstream vendorizados dentro de Mix-dev-ai.

Cada repo del manifiesto `upstream.json` se descarga en una cache git local
(`.cache/upstream/<name>`, ignorada por git) y desde ahí se copia a su carpeta
destino aplicando los filtros del perfil elegido. El resultado es una copia
"vendored": todo el código vive en este repo, así que un simple `git clone`
basta para que un agente de IA lo use.

Modos de uso:

    python3 scripts/sync-upstream.py --check            # ¿hay novedades? (no escribe nada)
    python3 scripts/sync-upstream.py                    # sincroniza con el perfil por defecto
    python3 scripts/sync-upstream.py --profile slim     # sólo código fuente (repo ligero)
    python3 scripts/sync-upstream.py --profile full     # copia literal del upstream
    python3 scripts/sync-upstream.py --repo rea         # sincroniza uno solo
    python3 scripts/sync-upstream.py --pin rea <sha>    # fija un commit concreto (y lo respeta en futuras syncs)
    python3 scripts/sync-upstream.py --unpin rea        # vuelve a seguir HEAD de la rama
    python3 scripts/sync-upstream.py --commit           # crea un commit git con el resultado

Exit codes:
    0  todo OK (o sin cambios)
    2  --check y hay actualizaciones pendientes
    1  error
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "upstream.json"


# --------------------------------------------------------------------------- #
# utilidades
# --------------------------------------------------------------------------- #
def die(msg: str, code: int = 1) -> "NoReturn":  # type: ignore[valid-type]
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(code)


def run(args: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=str(cwd) if cwd else None, check=check,
                          capture_output=True, text=True)


def human(n: int) -> str:
    step = 1024.0
    for unit in ("B", "KB", "MB", "GB"):
        if n < step or unit == "GB":
            return f"{n:.1f} {unit}" if unit != "B" else f"{n} B"
        n /= step
    return f"{n:.1f} GB"


def load_manifest() -> dict:
    if not MANIFEST.exists():
        die(f"no existe el manifiesto {MANIFEST}")
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for repo in data["repos"]:
        repo.setdefault("branch", "main")
        repo.setdefault("pin", None)
        repo.setdefault("groups", [])
        repo.setdefault("exclude", [])
        repo.setdefault("keep", [])
    return data


def patterns_for(manifest: dict, repo: dict, profile_name: str) -> tuple[list[str], int | None]:
    """Devuelve (patrones_excluidos, max_bytes) para un repo + perfil."""
    profile = manifest["profiles"][profile_name]
    pats: list[str] = []
    for group in profile["groups"] + repo["groups"]:
        pats.extend(manifest["groups"].get(group, []))
    pats.extend(repo["exclude"])
    pats.extend(manifest.get("exclude", []))
    # los `keep` ganan siempre
    return sorted(set(pats)), profile.get("max_bytes")


def is_excluded(rel: str, patterns: list[str], keep: list[str]) -> bool:
    rel = rel.replace(os.sep, "/")
    base = rel.rsplit("/", 1)[-1]
    for k in keep:
        k = k.replace(os.sep, "/")
        if fnmatch.fnmatch(rel, k) or fnmatch.fnmatch(base, k):
            return False
    for p in patterns:
        p = p.replace(os.sep, "/")
        if p.endswith("/**"):
            head = p[:-3]
            if rel == head or rel.startswith(head + "/"):
                return True
        if fnmatch.fnmatch(rel, p) or fnmatch.fnmatch(base, p):
            return True
    return False


# --------------------------------------------------------------------------- #
# git cache
# --------------------------------------------------------------------------- #
def ensure_cache(manifest: dict, repo: dict) -> Path:
    cache_dir = ROOT / manifest.get("cache_dir", ".cache/upstream")
    cache = cache_dir / repo["name"]
    cache.parent.mkdir(parents=True, exist_ok=True)
    if not (cache / "HEAD").exists():
        run(["git", "init", "--bare", "--quiet", str(cache)])
    git = ["git", "--git-dir", str(cache)]
    if run(git + ["remote", "get-url", "origin"], check=False).returncode != 0:
        run(git + ["remote", "add", "origin", repo["url"]], check=False)
    else:
        run(git + ["remote", "set-url", "origin", repo["url"]], check=False)
    run(git + ["config", "remote.origin.fetch",
               "+refs/heads/*:refs/remotes/origin/*"], check=False)
    return cache


def fetch(cache: Path, repo: dict, depth: int) -> None:
    """Trae el ref (rama o sha fijado) a la cache. Prueba superficial -> completo."""
    ref = repo["pin"] or repo["branch"]
    attempts: list[list[str]] = []
    if depth > 0:
        attempts.append([f"--depth={depth}"])
    attempts.append([])                 # historial completo del ref
    attempts.append(["--unshallow"])    # cache previamente superficial
    last = ""
    for extra in attempts:
        cmd = ["git", "--git-dir", str(cache), "fetch", "--quiet", "--force",
               "--tags", *extra, "origin", ref]
        proc = run(cmd, check=False)
        if proc.returncode == 0:
            return
        last = (proc.stderr or "").strip()
    die(f"no se pudo hacer fetch de {repo['url']} ({ref}): {last}")


def resolve_commit(cache: Path, repo: dict) -> dict:
    ref = repo["pin"] or "FETCH_HEAD"
    proc = run(["git", "--git-dir", str(cache), "rev-parse", ref], check=False)
    if proc.returncode != 0:
        die(f"no se pudo resolver {ref} en la cache de {repo['name']}")
    sha = proc.stdout.strip()
    fmt = "%cI%x00%s%x00%an"
    proc = run(["git", "--git-dir", str(cache), "log", "-1", f"--format={fmt}", sha], check=False)
    date, subject, author = (proc.stdout.strip("\n").split("\0") + ["", "", ""])[:3]
    return {"commit": sha, "commit_date": date, "subject": subject, "author": author}


# --------------------------------------------------------------------------- #
# materialización
# --------------------------------------------------------------------------- #
def export_tree(cache: Path, sha: str, dest: Path) -> None:
    """Extrae el árbol del commit `sha` en `dest` usando `git archive` (streaming)."""
    dest.mkdir(parents=True, exist_ok=True)
    # --prefix= garantiza que git no anteponga ningún directorio al árbol
    proc = subprocess.Popen(["git", "--git-dir", str(cache), "archive", "--prefix=",
                             "--format=tar", sha],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert proc.stdout is not None
    with tarfile.open(fileobj=proc.stdout, mode="r|") as tar:
        for member in tar:
            if member.isdir() or member.issym() or not member.isfile():
                continue
            rel = member.name
            while rel.startswith("./"):
                rel = rel[2:]
            if not rel:
                continue
            target = dest / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            extracted = tar.extractfile(member)
            if extracted is None:
                continue
            with extracted as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst)
            mode = member.mode & 0o777
            if member.mode & 0o100:
                mode |= 0o111
            try:
                target.chmod(mode)
            except OSError:
                pass
    err = proc.stderr.read().decode() if proc.stderr else ""
    proc.wait()
    if proc.returncode != 0:
        die(f"git archive falló para {sha}: {err.strip()}")


def prune_and_copy(src: Path, dst: Path, patterns: list[str], keep: list[str],
                   max_bytes: int | None, dry_run: bool) -> dict:
    """Copia src -> dst aplicando excludes y borra lo que ya no existe upstream."""
    wanted: dict[str, int] = {}
    skipped_bytes = 0
    skipped_files = 0

    for path in src.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        rel = path.relative_to(src).as_posix()
        if is_excluded(rel, patterns, keep):
            skipped_files += 1
            skipped_bytes += path.stat().st_size
            continue
        if max_bytes and path.stat().st_size > max_bytes:
            skipped_files += 1
            skipped_bytes += path.stat().st_size
            continue
        wanted[rel] = path.stat().st_size

    stats = {"files": len(wanted), "bytes": sum(wanted.values()),
             "skipped_files": skipped_files, "skipped_bytes": skipped_bytes,
             "added": 0, "changed": 0, "removed": 0}

    if dry_run:
        return stats

    dst.mkdir(parents=True, exist_ok=True)
    # borrar lo que ya no está upstream
    for path in sorted(dst.rglob("*"), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()
            continue
        if not path.is_file():
            continue
        rel = path.relative_to(dst).as_posix()
        if rel not in wanted:
            path.unlink()
            stats["removed"] += 1
    for path in sorted(dst.rglob("*"), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            try:
                path.rmdir()
            except OSError:
                pass

    for rel, size in wanted.items():
        target = dst / rel
        source = src / rel
        existed = target.exists()
        if existed and target.stat().st_size == size:
            continue  # mismo tamaño y el sha upstream ya cambió: no lo recopiamos
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        stats["changed" if existed else "added"] += 1
    return stats


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description="Sincroniza los repos upstream vendorizados.")
    ap.add_argument("--profile", default=None, help="perfil de exclusión (full|lean|slim)")
    ap.add_argument("--repo", action="append", default=[], help="sólo este repo (repetible)")
    ap.add_argument("--check", action="store_true", help="comprueba si hay novedades sin escribir")
    ap.add_argument("--force", action="store_true", help="rematerializa aunque el commit no cambie")
    ap.add_argument("--pin", nargs=2, metavar=("REPO", "SHA"), help="fija un repo a un commit")
    ap.add_argument("--unpin", metavar="REPO", help="un repo vuelve a seguir HEAD de su rama")
    ap.add_argument("--depth", type=int, default=None, help="profundidad de fetch (0 = historial completo)")
    ap.add_argument("--commit", action="store_true", help="crea un commit git con el resultado")
    ap.add_argument("--no-fetch", action="store_true", help="usa la cache local sin consultar la red")
    args = ap.parse_args()

    manifest = load_manifest()
    profile_name = args.profile or manifest.get("default_profile", "lean")
    if profile_name not in manifest["profiles"]:
        die(f"perfil desconocido '{profile_name}'. Disponibles: {', '.join(manifest['profiles'])}")

    if args.pin:
        name, sha = args.pin
        entry = next((r for r in manifest["repos"] if r["name"] == name), None)
        if entry is None:
            die(f"repo '{name}' no está en el manifiesto")
        entry["pin"] = sha
        text = json.dumps(manifest, indent=2, ensure_ascii=False)
        MANIFEST.write_text(text + "\n", encoding="utf-8")
        print(f"[pin] {name} -> {sha}")
    if args.unpin:
        entry = next((r for r in manifest["repos"] if r["name"] == args.unpin), None)
        if entry is None:
            die(f"repo '{args.unpin}' no está en el manifiesto")
        entry["pin"] = None
        MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                            encoding="utf-8")
        print(f"[pin] {args.unpin} -> sigue HEAD de {entry['branch']}")

    state_path = ROOT / manifest.get("state_file", ".upstream-state.json")
    state: dict = {}
    if state_path.exists():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            state = {}
    state.setdefault("repos", {})

    repos = [r for r in manifest["repos"] if not args.repo or r["name"] in args.repo]
    if not repos:
        die(f"ningún repo coincide con {args.repo}")

    pending = False
    touched: list[str] = []

    with tempfile.TemporaryDirectory(prefix="upstream-") as tmp:
        tmpdir = Path(tmp)
        for repo in repos:
            name = repo["name"]
            patterns, max_bytes = patterns_for(manifest, repo, profile_name)
            print(f"\n=== {name} ({repo['url']}) ===")
            cache = ensure_cache(manifest, repo)
            if not args.no_fetch:
                fetch(cache, repo, args.depth if args.depth is not None
                      else int(manifest.get("fetch_depth", 1)))
            info = resolve_commit(cache, repo)
            prev = state["repos"].get(name, {})
            print(f"  upstream : {info['commit'][:12]}  {info['commit_date']}  {info['subject'][:60]}")
            print(f"  local    : {(prev.get('commit') or '—')[:12]}  {prev.get('synced_at', '—')}")

            changed = args.force or prev.get("commit") != info["commit"] \
                or prev.get("profile") != profile_name
            if args.check:
                if changed:
                    pending = True
                    print(f"  -> ACTUALIZACIÓN DISPONIBLE ({prev.get('commit','—')[:12]} -> {info['commit'][:12]})")
                else:
                    print("  -> al día")
                continue
            if not changed:
                print("  -> al día, nada que hacer")
                continue

            work = tmpdir / name
            if work.exists():
                shutil.rmtree(work)
            export_tree(cache, info["commit"], work)
            stats = prune_and_copy(work, ROOT / repo["path"], patterns, repo["keep"],
                                   max_bytes, dry_run=False)
            print(f"  -> {stats['files']} ficheros ({human(stats['bytes'])}) "
                  f"| +{stats['added']} ~{stats['changed']} -{stats['removed']} "
                  f"| filtrados {stats['skipped_files']} ({human(stats['skipped_bytes'])})")
            state["repos"][name] = {
                "path": repo["path"],
                "url": repo["url"],
                "branch": repo["branch"],
                "pin": repo["pin"],
                "profile": profile_name,
                "files": stats["files"],
                "bytes": stats["bytes"],
                "synced_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                **info,
            }
            touched.append(name)
            shutil.rmtree(work, ignore_errors=True)

    if args.check:
        print("\nHay actualizaciones pendientes." if pending else "\nTodo al día.")
        return 2 if pending else 0

    if touched:
        state["synced_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        state["profile"] = profile_name
        state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n",
                              encoding="utf-8")
        print(f"\nEstado guardado en {state_path.relative_to(ROOT)}")

        if args.commit:
            summary = ", ".join(
                f"{n}@{state['repos'][n]['commit'][:8]}" for n in touched)
            msg = f"chore(upstream): sync {summary}"
            run(["git", "add", "-A", "--", *[state["repos"][n]["path"] for n in touched],
                 str(state_path.relative_to(ROOT)), MANIFEST.relative_to(ROOT)], cwd=ROOT)
            status = run(["git", "diff", "--cached", "--quiet"], cwd=ROOT, check=False)
            if status.returncode != 0:
                run(["git", "commit", "-m", msg], cwd=ROOT)
                print(f"commit creado: {msg}")
            else:
                print("sin cambios que commitear")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
