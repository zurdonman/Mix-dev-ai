#!/usr/bin/env python3
"""Genera los artefactos "de lectura" del grafo: GRAPH_REPORT.md, graph.html y wiki/.

Es un envoltorio fino alrededor de la API de graphify. Existe por dos motivos:

  * `graphify cluster-only` aborta su escritura cuando el número de nodos baja
    aunque sea en 1 (protección anti-pérdida de datos #479 de graphify). Como este
    repo hace un rebuild completo y determinista desde el código vendorizado,
    esa comprobación no aporta nada y sí rompe la automatización.
  * Permite dejar el etiquetado de comunidades sin LLM (determinista, coste 0)
    y decidir el límite de nodos del HTML.

Uso:
    python3 scripts/graph-report.py                # todo
    python3 scripts/graph-report.py --no-html      # sin graph.html (grafo grande)
    python3 scripts/graph-report.py --node-limit 800
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "graphify-out"
GRAPH = OUT / "graph.json"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--graph", default=str(GRAPH))
    ap.add_argument("--node-limit", type=int,
                    default=int(os.environ.get("GRAPHIFY_VIZ_NODE_LIMIT", "800")))
    ap.add_argument("--no-html", action="store_true")
    ap.add_argument("--no-wiki", action="store_true")
    ap.add_argument("--top-gods", type=int, default=15)
    args = ap.parse_args()

    graph_path = Path(args.graph)
    if not graph_path.exists():
        print(f"error: no existe {graph_path}. Ejecuta antes: graphify extract . --code-only --out .",
              file=sys.stderr)
        return 1
    out = graph_path.parent

    from graphify.build import build_from_json
    from graphify.cluster import (cluster, score_all, label_communities_by_hub,
                                  community_member_sigs, remap_communities_to_previous)
    from graphify.analyze import god_nodes, surprising_connections, suggest_questions
    from graphify.report import generate
    from graphify.export import to_json
    from graphify.exporters.html import to_html
    from graphify.wiki import to_wiki

    print(f"[1/6] cargando {graph_path} ({graph_path.stat().st_size / 1048576:.1f} MiB)")
    raw = json.loads(graph_path.read_text(encoding="utf-8"))
    directed = bool(raw.get("directed", False))
    G = build_from_json(raw, directed=directed)
    print(f"      {G.number_of_nodes()} nodos, {G.number_of_edges()} aristas")

    prev_map = {n["id"]: n["community"] for n in raw.get("nodes", [])
                if n.get("id") is not None and n.get("community") is not None}

    print("[2/6] comunidades (Leiden)")
    communities = cluster(G)
    communities = remap_communities_to_previous(communities, prev_map)
    cohesion = score_all(G, communities)
    print(f"      {len(communities)} comunidades")

    labels_path = out / ".graphify_labels.json"
    sig_path = out / (labels_path.name + ".sig")
    labels: dict[int, str] = {}
    if labels_path.exists() and sig_path.exists():
        try:
            saved = {int(k): v for k, v in json.loads(labels_path.read_text()).items()}
            sigs = {int(k): v for k, v in json.loads(sig_path.read_text()).items()}
            cur = community_member_sigs(communities)
            labels = {cid: saved[cid] for cid in communities
                      if saved.get(cid) and saved.get(cid) != f"Community {cid}"
                      and sigs.get(cid) == cur.get(cid)}
        except (ValueError, KeyError):
            labels = {}
    missing = [cid for cid in communities if cid not in labels]
    if missing:
        hub = label_communities_by_hub(G, {cid: communities[cid] for cid in missing})
        labels.update(hub)

    print("[3/6] god nodes / sorpresas / preguntas")
    gods = god_nodes(G, top_n=args.top_gods)
    surprises = surprising_connections(G, communities, top_n=8)
    questions = suggest_questions(G, communities, labels, top_n=7)

    print("[4/6] graph.json actualizado")
    to_json(G, communities, str(out / "graph.json"), force=True,
            community_labels=labels,
            built_at_commit=raw.get("built_at_commit"),
            original_links=raw.get("links") or raw.get("edges") or [])

    print("[5/6] GRAPH_REPORT.md + .graphify_analysis.json")
    try:
        from graphify.report import load_learning_for_report
        learning = load_learning_for_report(out / "graph.json")
    except Exception:
        learning = None
    report = generate(G, communities, cohesion, labels, gods, surprises,
                      {"warning": "rebuild completo desde el código vendorizado"},
                      {"input": 0, "output": 0}, str(ROOT),
                      suggested_questions=questions, built_at_commit=raw.get("built_at_commit"),
                      learning=learning)
    report += _local_footer(G, communities, gods)
    (out / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    analysis = {
        "communities": {str(k): v for k, v in communities.items()},
        "cohesion": {str(k): v for k, v in cohesion.items()},
        "gods": gods, "surprises": surprises, "questions": questions,
    }
    (out / ".graphify_analysis.json").write_text(
        json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8")
    (labels_path).write_text(
        json.dumps({str(k): v for k, v in labels.items()}, indent=2, ensure_ascii=False),
        encoding="utf-8")
    sig_path.write_text(json.dumps({str(k): v for k, v in
                                    community_member_sigs(communities).items()}),
                        encoding="utf-8")

    if not args.no_html:
        print(f"[6/6] graph.html (límite {args.node_limit} nodos; agrega por comunidad si hace falta)")
        try:
            ok = to_html(G, communities, str(out / "graph.html"),
                         community_labels=labels or None, node_limit=args.node_limit)
            print("      graph.html escrito" if ok else "      graph.html omitido")
        except ValueError as exc:
            print(f"      graph.html omitido: {exc}")

    if not args.no_wiki:
        print("[+]   wiki/")
        n = to_wiki(G, communities, str(out / "wiki"), community_labels=labels or None,
                    cohesion=cohesion, god_nodes_data=gods)
        print(f"      {n} artículos -> {out}/wiki/index.md")

    print("\nHecho. Entry points: graphify-out/GRAPH_REPORT.md | wiki/index.md | graph.html")
    return 0


def _local_footer(G, communities, gods) -> str:
    """Anexa un bloque en español con lo justo para orientar a un agente."""
    by_repo: dict[str, int] = {}
    for node, attrs in G.nodes(data=True):
        src = attrs.get("source_file") or ""
        top = src.split("/", 1)[0] if "/" in src else "(raíz)"
        by_repo[top] = by_repo.get(top, 0) + 1
    top = sorted(by_repo.items(), key=lambda kv: -kv[1])[:8]
    lines = ["", "---", "", "## Cómo usar este grafo (Mix-dev-ai)", "",
             "| Zona | Nodos |", "| --- | ---: |"]
    lines += [f"| `{k}` | {v} |" for k, v in top]
    lines += ["",
              "```bash",
              "graphify query \"<pregunta>\" --graph graphify-out/graph.json --budget 2000",
              "graphify path \"<A>\" \"<B>\" --graph graphify-out/graph.json",
              "graphify explain \"<concepto>\" --graph graphify-out/graph.json",
              "```",
              "",
              "El grafo se regenera con `make graph` y se mantiene al día con `make refresh`.",
              ""]
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
