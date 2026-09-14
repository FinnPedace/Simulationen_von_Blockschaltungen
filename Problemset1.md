## Problemset 1.1
### git status output :git status
On branch main
Your branch is up to date with 'origin/main'.

## Problemset 1.2

### a) Initialisieren einer Python-Bibliothek mit `uv`

Die Bibliothek wurde im Wurzelverzeichnis des Git-Repositories mit folgendem
Befehl initialisiert:

```bash
uv init --library
```

Dabei wurden unter anderem die folgenden Dateien erzeugt:

#### `pyproject.toml`

Diese Datei enthält die zentralen Projektinformationen und die Konfiguration
für den Build-Prozess:

- Der Paketname lautet `simulationen-von-blockschaltungen`.
- Die aktuelle Version ist `0.1.0`.
- Eine Beschreibung und die zugehörige README-Datei sind eingetragen.
- Als Autor ist Finn Pedace angegeben.
- Das Projekt benötigt Python `>=3.13`.
- Derzeit sind keine Abhängigkeiten eingetragen (`dependencies = []`).
- Als Build-System wird `uv_build` verwendet.

#### `src/simulationen_von_blockschaltungen/__init__.py`

Diese Datei markiert das Verzeichnis als Python-Paket und enthält den von `uv`
angelegten Beispielcode:

```python
def hello() -> str:
	return "Hello from simulationen-von-blockschaltungen!"
```

Der Paketname verwendet im Verzeichnis Unterstriche (`_`), während der
Projektname in `pyproject.toml` Bindestriche (`-`) enthält.

#### `.python-version`

In dieser Datei steht:

```text
3.13
```

Sie legt fest, dass für dieses Projekt Python 3.13 verwendet werden soll.

