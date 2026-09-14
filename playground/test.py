import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from Pauli_matrices import pauli_x, pauli_y, pauli_z
from simulationen_von_blockschaltungen import hello


print(hello())

sigma_x = pauli_x()
sigma_y = pauli_y()
sigma_z = pauli_z()

left_side = sigma_x @ sigma_y
right_side = 1j * sigma_z

print("sigma_x @ sigma_y:")
print(left_side)
print("i * sigma_z:")
print(right_side)
print("Relation holds:", np.allclose(left_side, right_side))

assert np.allclose(left_side, right_side)
