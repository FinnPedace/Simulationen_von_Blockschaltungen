# Cheatsheet: Simulationen von Blockschaltungen

Dieses Cheatsheet sammelt die wichtigsten Befehle und Vorgehensweisen aus dem
Projekt. Alle Befehle werden im Projektstamm ausgeführt.

## Projekt mit `uv` einrichten

```powershell
uv init --library
uv sync
uv add numpy
uv add ipykernel
```

`uv sync` erstellt `.venv/`, installiert die Abhängigkeiten aus
`pyproject.toml` und installiert das eigene Paket in die virtuelle Umgebung.

Aktuelle Abhängigkeiten:

- `numpy`: numerische Berechnungen und Matrizen
- `ipykernel`: Python-Kernel für Jupyter-Notebooks

## Python aus der Umgebung ausführen

```powershell
uv run python playground/test.py
uv run python -c "import sys; print(sys.executable)"
uv run python -c "from simulationen_von_blockschaltungen import hello; print(hello())"
```

## Pauli-Matrizen

Die Funktionen befinden sich in `src/Pauli_matrices.py`:

```python
from Pauli_matrices import pauli_x, pauli_y, pauli_z

sigma_x = pauli_x()
sigma_y = pauli_y()
sigma_z = pauli_z()
```

Matrixmultiplikation erfolgt mit `@`, nicht mit `*`:

```python
left_side = sigma_x @ sigma_y
right_side = 1j * sigma_z
assert np.allclose(left_side, right_side)
```

Damit wird numerisch überprüft:

$$\sigma_x\sigma_y = i\sigma_z$$

## Matrixfunktionen

Die Funktionen liegen im Paket unter `src/simulationen_von_blockschaltungen/`:

```python
from simulationen_von_blockschaltungen import matrix_product
from simulationen_von_blockschaltungen.matrix_sum import matrix_sum
```

`matrix_product` multipliziert Matrizen in der angegebenen Reihenfolge. Mit
`matrix_sum` werden Matrizen elementweise addiert. Beide Funktionen erwarten
NumPy-Arrays:

```python
product = matrix_product([sigma_x, sigma_y])
total = matrix_sum([sigma_x, sigma_y, sigma_z])
```

Für `matrix_product` müssen die Dimensionen kompatibel sein. Für `matrix_sum`
müssen alle Matrizen dieselbe Form haben.

## Gemeinsamer Funktionstest

Beide Funktionen lassen sich nach einem Merge direkt aus dem Projektstamm
prüfen:

```powershell
uv run python -c "import sys; import numpy as np; sys.path.insert(0, 'src'); from Pauli_matrices import pauli_x, pauli_y, pauli_z; from simulationen_von_blockschaltungen import matrix_product; from simulationen_von_blockschaltungen.matrix_sum import matrix_sum; sigma_x, sigma_y, sigma_z = pauli_x(), pauli_y(), pauli_z(); assert np.allclose(matrix_product([sigma_x, sigma_y]), 1j * sigma_z); assert np.array_equal(matrix_sum([sigma_x, sigma_y, sigma_z]), sigma_x + sigma_y + sigma_z); print('matrix_product: passed'); print('matrix_sum: passed')"
```

Erwartete Ausgabe:

```text
matrix_product: passed
matrix_sum: passed
```

## Jupyter-Notebooks

Das Notebook liegt unter `notebooks/pauli_matrices.ipynb`.

```powershell
uv run python -m ipykernel install --user `
	--name simulationen-von-blockschaltungen `
	--display-name "Python (simulationen-von-blockschaltungen)"
```

In VS Code oben rechts im Notebook den Kernel
`Python (simulationen-von-blockschaltungen)` auswählen. Alternativ über
`Ctrl+Shift+P` den Befehl `Notebook: Select Notebook Kernel` öffnen und
`.venv\Scripts\python.exe` auswählen.

Den verwendeten Interpreter kann man im Notebook prüfen:

```python
import sys

print(sys.executable)
```

## Ruff: Formatierung und Linting

```powershell
$env:UV_LINK_MODE = "copy"
uvx ruff check
uvx ruff check --fix
```

`I001 Import block is un-sorted or un-formatted` bedeutet, dass Ruff die
Importreihenfolge oder Formatierung beanstandet. Nach `--fix` Ruff erneut
ausführen.

## Pre-Commit-Hooks

Die Konfiguration steht in `.pre-commit-config.yaml`. Die Hooks prüfen
YAML-Dateien, Dateiendungen und Leerzeichen und formatieren Python-Dateien mit
Black.

```powershell
# Hooks im lokalen Repository installieren
$env:UV_LINK_MODE = "copy"
uvx pre-commit install

# Alle Dateien manuell prüfen
uvx pre-commit run --all-files
```

Nach einer automatischen Korrektur die Datei erneut stagen:

```powershell
git add <datei>
git commit -m "Beschreibung der Änderung"
```

Ein nachgestelltes Leerzeichen wird vom Hook `trailing-whitespace` erkannt,
entfernt und führt zunächst zu einem abgebrochenen Commit. Danach muss die
korrigierte Datei erneut gestaged werden.

## OneDrive-Problem mit `uv`

Bei Projekten in OneDrive kann `uv` beim Erstellen von Hardlinks den Fehler
`os error 396` ausgeben. Dann den Kopiermodus setzen:

```powershell
$env:UV_LINK_MODE = "copy"
```

Danach den gewünschten `uvx`-Befehl erneut ausführen. Das gilt insbesondere
für Ruff und Pre-Commit.

## Git-Grundbefehle

```powershell
# Status und Änderungen anzeigen
git status
git diff

# Änderungen vormerken
git add <datei>
git add .

# Commit erstellen
git commit -m "Kurze Beschreibung"

# Letzten Commit anzeigen
git log -1 --oneline
```

## Branches und Merge

```powershell
# Branches und aktiven Branch anzeigen
git branch

# Zielbranch auswählen
git switch main

# Fast-Forward, wenn main keine eigenen neuen Commits hat
git merge --ff-only matrix_sum

# Normaler Merge bei auseinanderentwickelten Branches
git merge matrix_product

# Historie kontrollieren
git log --oneline --decorate --graph --all
```

Vor dem Merge sollte der Arbeitsbaum sauber sein:
git status

## `.gitignore`

Diese Dateien und Ordner werden nicht versioniert:

```gitignore
local/
__pycache__/
.venv/
uv.lock
```

- `local/`: lokale Notizen
- `.venv/`: virtuelle Python-Umgebung
- `__pycache__/`: Python-Cache-Dateien
- `uv.lock`: Lock-Datei von `uv`
