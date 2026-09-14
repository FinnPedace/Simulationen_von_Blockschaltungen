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
Mit `print(greet("Finn"))` wäre der Aufruf typkorrekt und die Prüfung würde
erfolgreich durchlaufen.
