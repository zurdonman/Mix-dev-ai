# Mix-dev-ai

Monorepo de herramientas de IA para **modear juegos** y **hacer ingeniería inversa**, con un
**grafo de conocimiento del código** para que un agente (Claude Code, Codex, Cursor, Gemini CLI,
Aider, Copilot…) pueda trabajar sobre todo ello gastando el mínimo de tokens.

```
Mix-dev-ai/
├── README.md                  ← estás aquí
├── AGENTS.md                  ← reglas para agentes de IA (leer primero)
├── universal-modder/          ← copia completa de rehan-remade/universal-modder
├── rea/                       ← copia completa de morluto/rea
├── graphify-out/              ← grafo de código de TODO el repo
│   ├── GRAPH_REPORT.md            informe: god nodes, comunidades, conexiones raras
│   ├── wiki/index.md              navegación tipo Wikipedia (694 artículos)
│   └── graph.html                 grafo interactivo (se abre en el navegador)
├── upstream.json              ← manifiesto: de dónde viene cada carpeta y qué se copia
├── scripts/
│   ├── sync-upstream.py           trae la última versión de los repos originales
│   ├── build-graph.sh             reconstruye el grafo
│   └── graph-report.py            regenera informe + HTML + wiki
├── .github/workflows/sync-and-graph.yml   actualización automática nocturna
├── docs/
│   └── adb-android.md         ← guía: ADB desde el móvil con Termux (sin PC)
└── Makefile                   ← atajos: make check / sync / graph / refresh
```

---

## 1. Qué hay dentro

| Carpeta | Origen | Qué hace | Lenguaje | Licencia |
| --- | --- | --- | --- | --- |
| `universal-modder/` | [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) | Apunta Claude (o cualquier agente) a un juego y lo modea: reconocimiento, ingeniería inversa, assets con IA (fal), testing in-game, vídeos de showcase. Skills + CLI `um` + MCP. | Python | MIT |
| `rea/` | [morluto/rea](https://github.com/morluto/rea) | Ingeniería inversa con agentes: del comportamiento de una app hasta binarios nativos. Bridges a Ghidra / Hopper / IDA, análisis estático de JS/Electron, MCP propio. | TypeScript | MIT |

Ambas son copias **vendorizadas** (el código vive aquí dentro, sin submódulos): un
`git clone` normal lo trae todo, sin `--recurse-submodules`.

Detalles de la copia:

- Se quitan **media pesada y artefactos** (`.glb`, `.jpg`, GIFs, `.pdf`, fuentes, `node_modules`,
  `dist`, `__pycache__`, traducciones `.po`, `contributions.json` generados). El código, las
  skills, la documentación, los tests y los ejemplos se conservan.
- `universal-modder`: ~7 MB / 717 ficheros. `rea`: ~60 MB / 6.253 ficheros.
- El estado exacto (commit, fecha, nº de ficheros) está en [`.upstream-state.json`](.upstream-state.json).

> ⚠️ **No edites a mano** dentro de `universal-modder/` ni `rea/`: la siguiente sincronización
> sobrescribe y borra lo que no exista en el upstream. Tus cambios van en carpetas propias.

---

## 2. Empezar (humano o agente) en 30 segundos

```bash
git clone <este-repo> && cd Mix-dev-ai

# 2.1 ¿solo quiero usar las herramientas?
cat universal-modder/README.md
cat rea/README.md

# 2.2 ¿quiero el grafo consultable? (necesita graphify, sin API key)
pip install -r requirements-tools.txt     # instala graphify
make graph                                # ~4 min, AST local, coste 0

# 2.3 ya puedo preguntar al grafo
graphify query "cómo escanea un juego universal-modder" --graph graphify-out/graph.json
```

Si eres un agente: lee **[AGENTS.md](AGENTS.md)** y empieza por
`graphify-out/wiki/index.md` o `graphify-out/GRAPH_REPORT.md` en vez de recorrer ficheros.

---

## 3. El grafo de código (graphify)

[Graphify](https://github.com/Graphify-Labs/graphify) parsea el código con tree-sitter (AST, local,
determinista, **sin llamar a ningún LLM**) y construye un grafo de nodos (ficheros, funciones,
clases, conceptos) y aristas tipadas (`calls`, `imports`, `inherits`, `references`…). Después
agrupa el grafo en comunidades y genera material de navegación para el agente.

Estado actual de este repo:

| Métrica | Valor |
| --- | ---: |
| Nodos | **42.055** |
| Aristas | **165.093** (98 % extraídas del AST, 2 % inferidas) |
| Comunidades | 679 |
| Artículos de wiki | 694 |
| Nodos de `rea` / `universal-modder` | 37.218 / 3.515 |
| Aristas que cruzan entre los dos repos | 24 |
| Coste de generación | 0 tokens |

`graphify-out/graph.json` (~65 MB) **no se versiona**: es 100 % regenerable con `make graph`.
Lo que sí se versiona es lo barato de leer y lo que ahorra tokens:

| Fichero | Para qué |
| --- | --- |
| `graphify-out/GRAPH_REPORT.md` | Resumen de arquitectura: god nodes, comunidades, conexiones inesperadas, preguntas sugeridas. |
| `graphify-out/wiki/index.md` | Índice con un artículo por comunidad y por nodo central. Es el mejor punto de entrada para un agente. |
| `graphify-out/graph.html` | Vista interactiva (agregada por comunidad) para explorar a mano. |

### Consultas que ahorran tokens

```bash
G=graphify-out/graph.json

graphify query "Ghidra bridge" --graph $G --budget 1500   # subgrafo relevante, no ficheros enteros
graphify path "createServer" "toolContracts" --graph $G   # cómo se conectan dos cosas
graphify explain "ProcessOwnership" --graph $G            # un concepto y sus vecinos
graphify affected "processRunTokenParser" --graph $G      # qué se rompe si cambio X
graphify god-nodes --graph $G --top 15                    # los hubs arquitectónicos
make query Q="electron static analysis"                   # atajo
```

Trucos: si `explain` dice *ambiguous*, usa `ruta/fichero.ts::simbolo`. Si `query` trunca, sube
`--budget` o filtra con `--context call`.

### Habilitar `/graphify` en tu editor/agente

```bash
graphify install --platform claude     # también: codex, cursor, gemini, aider, copilot, opencode…
```

Instala la skill y las reglas para que el agente consulte el grafo antes de hacer `grep`.
`AGENTS.md` ya contiene esas reglas para los agentes que lo lean directamente.

---

## 4. Mantenerlo actualizado (lo importante)

Hay **tres formas**, de menos a más automática.

### 4.1 Manual, cuando quieras

```bash
make check     # ¿hay commits nuevos en los repos originales? (no escribe nada, exit 2 si hay)
make sync      # trae la última versión de las dos carpetas
make graph     # regenera el grafo (AST, sin API key)
make refresh   # sync + graph + commit   ← el "ponme al día" de un solo golpe
make status    # commit y tamaño actual de cada copia
```

### 4.2 Automático en GitHub (recomendado)

[`.github/workflows/sync-and-graph.yml`](.github/workflows/sync-and-graph.yml) corre **cada noche**
(y a mano desde *Actions → sync-upstream-and-graph → Run workflow*):

1. `scripts/sync-upstream.py` trae el último commit de cada repo original.
2. Si algo cambió, `scripts/build-graph.sh` reconstruye el grafo.
3. Hace commit y push de las carpetas, `.upstream-state.json` y `graphify-out/`.

Así el repo nunca se queda desactualizado aunque no lo abras en semanas. Notas:

- Necesita que en *Settings → Actions → General* esté permitido **“Read and write permissions”**
  para el `GITHUB_TOKEN` (es lo único que hay que tocar).
- El workflow no hace push si no hay cambios.
- Si prefieres PRs en vez de commits directos, cambia el paso final por
  [`peter-evans/create-pull-request`](https://github.com/peter-evans/create-pull-request).

### 4.3 Tu propio cron / CI

```bash
python3 scripts/sync-upstream.py --check && echo "al día" || make refresh
```

### Fijar una versión concreta

Si un upstream rompe algo y no quieres que se mueva:

```bash
python3 scripts/sync-upstream.py --pin rea 1173c0a9dc1b
python3 scripts/sync-upstream.py --unpin rea        # vuelve a seguir la rama
```

---

## 5. Añadir otro repo

Todo se define en [`upstream.json`](upstream.json). Basta con añadir una entrada:

```json
{
  "name": "otra-herramienta",
  "path": "otra-herramienta",
  "url": "https://github.com/usuario/otra-herramienta",
  "branch": "main",
  "pin": null,
  "groups": [],
  "exclude": ["**/*.mp4"],
  "keep":   ["docs/**"]
}
```

```bash
make sync && make graph
```

- `groups`: patrones glob extra que se excluyen (además del perfil).
- `exclude` / `keep`: exclusiones puntuales; `keep` gana siempre sobre cualquier exclusión.
- `profiles` en el manifiesto definen cuánto se copia:

| Perfil | Qué copia | Uso |
| --- | --- | --- |
| `lean` (por defecto) | código + docs + tests + ejemplos, sin media ni traducciones, sin ficheros > 2 MB | día a día |
| `slim` | solo código y docs esenciales (sin tests ni ejemplos) | repo ligero para prompts |
| `full` | copia literal del upstream (incluida media) | si necesitas assets reales |

---

## 6. Herramientas que te recomiendo añadir

Las que de verdad encajan con “modear juegos + ingeniería inversa + agentes”:

| Herramienta | Para qué te sirve aquí |
| --- | --- |
| **[ast-grep](https://github.com/ast-grep/ast-grep)** | Búsqueda y **reescritura estructural** (AST) en C#, Java, Lua, Python, TS… Es *la* navaja suiza para tocar código de juegos sin regex frágiles. Ideal para los `mashup` de dos juegos. |
| **[Serena](https://github.com/oraios/serena)** (MCP) | Navegación y edición semántica por LSP: “encuentra la definición”, “renombra símbolo”, “quién llama a esto”. Complementa a graphify: grafo para arquitectura, LSP para precisión. |
| **[codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Alternativa/complemento al grafo con búsqueda vectorial y Cypher, soporte multi-repo. Útil si algún día el grafo se te queda pequeño. |
| **graphify MCP** (`graphify --mcp`) | Expone el grafo como herramientas MCP; cualquier cliente (Claude Desktop, Cursor, Codex) consulta el grafo sin CLI. |
| **[Repomix](https://github.com/yamadashy/repomix)** | Empaqueta un subárbol en un solo fichero para pegar en el prompt (útil para las skills de `universal-modder`, que son pequeñas). |
| **[ripgrep](https://github.com/BurntSushi/ripgrep)** + `fd` | Búsqueda rápida respetando `.gitignore`: el “grep de apoyo” cuando el grafo no basta. |
| **[uv](https://github.com/astral-sh/uv)** | Ejecuta herramientas Python/MCP (`uvx serena`, `uvx repomix`) sin ensuciar el entorno. |
| **[Renovate](https://github.com/renovatebot/renovate)** | Mantiene actualizadas dependencias *de este repo* (no del código vendorizado): equivalente automático a lo que hace `make sync`. |
| **[git-lfs](https://github.com/git-lfs/git-lfs)** | Solo si algún día quieres el perfil `full` con `.glb`/`.jpg` grandes de `universal-modder`. |
| **[pre-commit](https://github.com/pre-commit/pre-commit)** | Engancha `make check` y un `graphify update .` a cada commit, sin depender de Actions. |
| **ADB vía Termux** | Depurar/controlar otro Android sin PC: [docs/adb-android.md](docs/adb-android.md) y `scripts/termux-adb-pair.sh`. |

MCP que ya vienen con las herramientas copiadas (no hay que añadir nada):

- `universal-modder/mcp.json` → MCP de **fal** (generación de imágenes, 3D, audio, vídeo).
- `rea/` → bridges MCP a **Ghidra, Hopper, IDA** y a binarios nativos.

---

## 7. Créditos y licencias

- `universal-modder` © [rehan-remade](https://github.com/rehan-remade/universal-modder) — MIT.
- `rea` © [morluto](https://github.com/morluto/rea) — MIT.
- Grafo generado con [Graphify](https://github.com/Graphify-Labs/graphify) (`graphifyy`, MIT).

Cada carpeta conserva su `LICENSE` original. Si redistribuyes, mantén los avisos de copyright.
Este repo solo agrega y sincroniza copias; no modifica el código de terceros.
