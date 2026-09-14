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

## Problemset 1.4

### c) Statische Typprüfung mit `mypy` als Pre-Commit-Hook

Für die statische Typprüfung wurde `mypy` als zusätzlicher Pre-Commit-Hook in
`.pre-commit-config.yaml` eingerichtet. Im Playground-Skript steht folgende
typisierte Funktion:

```python
def greet(name: str) -> str:
    return "Hello, " + name


print(greet(42))
```

Der Aufruf `greet(42)` ist absichtlich falsch, da die Funktion einen String
(`str`) erwartet, aber eine Ganzzahl (`int`) erhält. Der Hook wurde mit
folgendem Befehl ausgeführt:

```powershell
uvx pre-commit run mypy --all-files
```

Dabei wurde folgender Fehler ausgegeben:

```text
mypy.....................................................................Failed
- hook id: mypy
- exit code: 1

playground\test.py:17: error: Argument 1 to "greet" has incompatible type "int";
expected "str"  [arg-type]
Found 1 error in 1 file (checked 3 source files)
```

Damit wurde nachgewiesen, dass `mypy` den Typfehler vor dem Commit erkennt.
Mit `print(greet("Einstein"))` wäre der Aufruf typkorrekt und die Prüfung würde
erfolgreich durchlaufen.

### d) Weitere Python-Tools und Konfigurationsmöglichkeiten

Bei der Recherche in der offiziellen Ruff- und mypy-Dokumentation wurden
folgende nützliche Möglichkeiten gefunden.

#### Ruff

Ruff übernimmt sowohl Linting als auch Formatierung und unterstützt neben
Python-Dateien auch Jupyter-Notebooks.

```powershell
# Linting ausführen
uvx ruff check

# Automatisch behebbare Linting-Probleme korrigieren
uvx ruff check --fix

# Formatierung prüfen, ohne Dateien zu verändern
uvx ruff format --check

# Dateien formatieren
uvx ruff format

# Erklärungen zu einer bestimmten Regel anzeigen
uvx ruff rule NPY201
```

Zusätzlich zur bereits aktivierten NPY-Regelgruppe könnten beispielsweise
folgende Regelgruppen aktiviert werden:

- `B`: Bugbear-Regeln für typische Fehler und problematische Konstruktionen
- `I`: Sortierung und Organisation von Imports
- `UP`: Modernisierung älterer Python-Syntax
- `RUF`: Ruff-spezifische Regeln
- `ANN`: zusätzliche Prüfung von Typannotationen

Die Auswahl erfolgt in `pyproject.toml` zum Beispiel so:

```toml
[tool.ruff.lint]
extend-select = ["NPY", "B", "I", "UP", "RUF"]
```

Weitere hilfreiche Ruff-Einstellungen sind:

```toml
[tool.ruff]
target-version = "py313"
line-length = 88

[tool.ruff.lint.per-file-ignores]
"notebooks/*.ipynb" = ["T201"]
```

Mit `target-version` wird die minimale Python-Version festgelegt. Ein
`per-file-ignores`-Eintrag kann einzelne Regeln für bestimmte Dateien oder
Verzeichnisse deaktivieren.

#### mypy

Mypy kann über eine `[tool.mypy]`-Sektion in `pyproject.toml` konfiguriert
werden. Ein strengerer Einstieg wäre:

```toml
[tool.mypy]
python_version = "3.13"
warn_return_any = true
warn_unused_configs = true
```

Für ein vollständig strenges Projekt kann später auch Folgendes verwendet
werden:

```toml
[tool.mypy]
strict = true
```

`strict = true` aktiviert viele optionale Prüfungen auf einmal. Deshalb ist es
sinnvoll, zunächst mit einzelnen Optionen zu beginnen und bestehende Fehler
schrittweise zu beheben.

Weitere mögliche Python-Tools sind:

- `pytest` für automatisierte Tests
- `coverage.py` beziehungsweise `pytest-cov` für Testabdeckung
- `pyright` oder `ty` als Alternativen zu `mypy` für statische Typprüfung
- `pre-commit` zur automatischen Ausführung von Qualitätsprüfungen vor jedem
    Commit

Quellen:

- [Ruff-Konfiguration](https://docs.astral.sh/ruff/configuration/)
- [Ruff-Regeln](https://docs.astral.sh/ruff/rules/)
- [mypy-Konfiguration](https://mypy.readthedocs.io/en/stable/config_file.html)

## Problemset 1.5

### Branches mit `git branch` untersuchen

Mit dem Befehl `git branch` wurden die vorhandenen Branches angezeigt:

```text
* main
    matrix_product
    matrix_sum
```

Der Stern `*` kennzeichnet den aktuell ausgewählten Branch. Ich befinde mich
demnach momentan auf dem Branch `main`.
