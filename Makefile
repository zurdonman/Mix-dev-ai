# Mix-dev-ai — utilidades
#
#   make check      ¿hay novedades en los repos originales? (no escribe nada)
#   make sync       trae la última versión de universal-modder y rea
#   make graph      regenera el grafo de código (AST local, sin API key)
#   make graph-deep igual + aristas semánticas con LLM (requiere API key)
#   make refresh    sync + graph + commit  (el "mantenlo al día" de un solo golpe)
#   make install    instala las herramientas (graphify)
#   make query Q="…"  pregunta al grafo
#   make clean      borra caches locales

SHELL := /bin/bash
GRAPHIFY ?= graphify
PROFILE ?= lean

.PHONY: help install check sync graph graph-deep refresh clean status query

help:
	@grep -E '^#   make' Makefile | sed 's/^#   //'

install:
	pip install -r requirements-tools.txt

check:
	python3 scripts/sync-upstream.py --check --profile $(PROFILE)

sync:
	python3 scripts/sync-upstream.py --profile $(PROFILE)

graph:
	GRAPHIFY="$(GRAPHIFY)" ./scripts/build-graph.sh code

graph-deep:
	GRAPHIFY="$(GRAPHIFY)" ./scripts/build-graph.sh deep

refresh:
	python3 scripts/sync-upstream.py --profile $(PROFILE)
	GRAPHIFY="$(GRAPHIFY)" ./scripts/build-graph.sh code
	@if [ -n "$$(git status --porcelain)" ]; then \
		git add -A -- universal-modder rea .upstream-state.json upstream.json graphify-out; \
		git commit -m "chore(upstream): sync + grafo $$(date +%F)"; \
		echo "commit creado"; \
	else \
		echo "sin cambios"; \
	fi

query:
	@test -n "$(Q)" || { echo 'uso: make query Q="tu pregunta"'; exit 1; }
	graphify query "$(Q)" --graph graphify-out/graph.json --budget $${BUDGET:-2000}

status:
	@python3 - <<'PY'
	import json
	s = json.load(open(".upstream-state.json"))
	for name, r in s["repos"].items():
		print(f"{name:<20} {r['commit'][:12]}  {r['commit_date'][:10]}  {r['files']:>5} ficheros  {r['bytes']/1048576:6.1f} MiB")
	PY

clean:
	rm -rf .cache
