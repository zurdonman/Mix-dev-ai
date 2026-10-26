# AGENTS.md — cómo trabajar en este repo (para Claude Code, Codex, Cursor, Copilot, etc.)

Este repo es un **monorepo de herramientas vendorizadas + un grafo de código** para que un
agente de IA pueda trabajar sobre ellas gastando el mínimo de tokens.

```
Mix-dev-ai/
├── universal-modder/   copia de rehan-remade/universal-modder   (modding de juegos)
├── rea/                copia de morluto/rea                     (reverse engineering)
├── graphify-out/       el grafo de código de TODO lo anterior
│   ├── GRAPH_REPORT.md     ← visión general: god nodes, comunidades, conexiones
│   ├── wiki/index.md       ← navegación tipo Wikipedia para agentes
│   ├── graph.html          ← grafo interactivo para humanos
│   └── graph.json          ← el grafo consultable (se regenera con `make graph`)
├── upstream.json           manifiesto de repos + reglas de copia
└── scripts/
    ├── sync-upstream.py    trae la última versión de los repos originales
    └── build-graph.sh      reconstruye el grafo
```

## Reglas (léelas antes de tocar código)

1. **Consulta el grafo antes de grepear.** Si `graphify-out/graph.json` existe, ejecuta
   `graphify query "<pregunta>"` antes de tu primer `grep`, búsqueda o lectura de fichero
   sobre el código. Usa `graphify path "<A>" "<B>"` para relaciones y
   `graphify explain "<concepto>"` para un concepto concreto. Devuelven un subgrafo acotado,
   mucho más pequeño que volcar ficheros. Pon esta regla también en el prompt de cualquier
   subagente que explore código.
2. **Navegación amplia → `graphify-out/wiki/index.md`**, no pasear ficheros al azar.
3. **`graphify-out/GRAPH_REPORT.md`** sólo para revisión de arquitectura global, o si
   query/path/explain no dan suficiente contexto.
4. **Lee el fichero original sólo para las líneas que el grafo ya te localizó.**
5. Después de modificar código en `universal-modder/` o `rea/`, ejecuta `graphify update .`
   (AST, sin coste de API) para que el grafo no se quede viejo.
6. `graphify-out/graph.json` se reescribe entero en cada build: un diff gigante es normal,
   no lo marques como ruido ni propongas saltarte el rebuild.
7. **No edites a mano** `universal-modder/` ni `rea/` salvo que el usuario lo pida: son copias
   de repos ajenos y la siguiente sincronización (`make sync`) las sobreescribirá. Si necesitas
   un cambio permanente, ponlo en una carpeta propia fuera de esas dos.

## Extras

- `docs/adb-android.md` + `scripts/termux-adb-pair.sh`: ADB inalámbrico desde Termux
  (`pkg install android-tools`, `adb pair`, `adb connect`). No confundir con `sdb`, que es de Tizen.

## Comandos

```bash
make install                                   # pip install -r requirements-tools.txt
make check                                     # ¿hay novedades upstream? (no escribe)
make sync                                      # actualiza las dos copias vendorizadas
make graph                                     # regenera el grafo (AST local, sin API key)
make graph-deep                                # + aristas semánticas con LLM (requiere API key)
make refresh                                   # sync + graph + commit
make status                                    # commits y tamaños actuales de cada copia
make query Q="electron static analysis"        # atajo de graphify query
```

Sin `graphify` instalado, el agente puede igualmente leer `graphify-out/wiki/index.md` y
`GRAPH_REPORT.md`, que sí están versionados.

## Consultas útiles de ejemplo

```bash
graphify query "cómo escanea un juego universal-modder" --graph graphify-out/graph.json --budget 2000
graphify query "Ghidra bridge" --graph graphify-out/graph.json
graphify path "scan" "GameEntry" --graph graphify-out/graph.json
graphify explain "ReaReverseTools" --graph graphify-out/graph.json
graphify affected "processRunTokenParser" --graph graphify-out/graph.json
graphify god-nodes --graph graphify-out/graph.json --top 15
```

## graphify

Este proyecto tiene un grafo de conocimiento en `graphify-out/` con god nodes, comunidades y
relaciones entre ficheros.

Cuando el usuario escriba `/graphify`, usa la skill de graphify (o estas instrucciones) antes
de cualquier otra cosa.
