#!/usr/bin/env bash
# (Re)construye el grafo de código de todo el repo con graphify.
#
#   ./scripts/build-graph.sh            # modo code: AST local, sin API key (determinista)
#   ./scripts/build-graph.sh deep       # modo deep: + aristas semánticas vía LLM
#   GRAPHIFY_VIZ_NODE_LIMIT=1500 ./scripts/build-graph.sh   # HTML con más nodos
#
# Salida en graphify-out/: graph.json, GRAPH_REPORT.md, graph.html, wiki/
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

GRAPHIFY="${GRAPHIFY:-graphify}"
MODE="${1:-code}"

# El script de informe importa el paquete `graphify`: necesitamos un python que lo
# tenga instalado. Si el `python3` del PATH no lo ve, probamos con el intérprete
# que acompaña al ejecutable de graphify (pipx/venv instalan ahí).
if [[ -z "${PYTHON:-}" ]]; then
  if python3 -c "import graphify" >/dev/null 2>&1; then
    PY=python3
  else
    candidate="$(dirname "$(command -v "$GRAPHIFY")")/python3"
    if [[ -x "$candidate" ]] && "$candidate" -c "import graphify" >/dev/null 2>&1; then
      PY="$candidate"
    else
      PY=python3
    fi
  fi
else
  PY="$PYTHON"
fi

command -v "$GRAPHIFY" >/dev/null 2>&1 || {
  echo "No encuentro 'graphify' en el PATH. Instálalo con:  pip install -r requirements-tools.txt" >&2
  exit 1
}

# graphify aborta si el grafo nuevo tiene menos nodos que el anterior (#479).
# Este repo siempre hace un rebuild completo desde código vendorizado, así que
# partimos de cero para que la comprobación no bloquee la automatización.
if [[ "${1:-}" != "update" ]]; then
  rm -f graphify-out/graph.json
fi

ARGS=(extract . --out .)
if [[ "$MODE" == "deep" ]]; then
  echo "==> [deep] extracción AST + semántica (LLM)"
  ARGS+=(--mode deep)
  [[ -n "${GRAPHIFY_BACKEND:-}" ]] && ARGS+=(--backend "$GRAPHIFY_BACKEND")
  [[ -n "${GRAPHIFY_MODEL:-}" ]] && ARGS+=(--model "$GRAPHIFY_MODEL")
else
  echo "==> [code] extracción AST local (sin API key)"
  ARGS+=(--code-only)
fi
[[ -n "${GRAPHIFY_MAX_WORKERS:-}" ]] && ARGS+=(--max-workers "$GRAPHIFY_MAX_WORKERS")

"$GRAPHIFY" "${ARGS[@]}" 2>&1 | grep -v "WARNING: node '" || true

echo "==> comunidades, informe, HTML y wiki"
if [[ "$MODE" == "deep" && -z "${GRAPHIFY_NO_LABEL:-}" ]]; then
  # en deep dejamos que graphify etiquete comunidades con el LLM configurado
  "$GRAPHIFY" cluster-only . 2>&1 | grep -v "WARNING: node '" || true
else
  "$PY" scripts/graph-report.py
fi

echo
echo "Listo. Empieza por graphify-out/GRAPH_REPORT.md y consulta con:"
echo "  graphify query \"<pregunta>\" --graph graphify-out/graph.json --budget 2000"
