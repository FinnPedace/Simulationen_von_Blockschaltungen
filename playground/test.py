import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from Pauli_matrices import pauli_x, pauli_y, pauli_z
from simulationen_von_blockschaltungen import hello
from simulationen_von_blockschaltungen.matrix_product import matrix_product
from simulationen_von_blockschaltungen.matrix_sum import matrix_sum


def greet(name: str) -> str:
    return "Hello, " + name


print(hello())

sigma_x = pauli_x()
sigma_y = pauli_y()
sigma_z = pauli_z()

left_side = sigma_x @ sigma_y
right_side = 1j * sigma_z
result = matrix_product([pauli_x(), pauli_y()])
expected = 1j * pauli_z()

print(result)
print(expected)
print("Relation holds:", np.allclose(result, expected))

assert np.allclose(result, expected)
print("sigma_x @ sigma_y:")
print(left_side)
print("i * sigma_z:")
print(right_side)
print("Relation holds:", np.allclose(left_side, right_side))

assert np.allclose(left_side, right_side)

sum_result = matrix_sum([sigma_x, sigma_y, sigma_z])
sum_expected = sigma_x + sigma_y + sigma_z

print("sigma_x + sigma_y + sigma_z:")
print(sum_result)
print("Sum correct:", np.array_equal(sum_result, sum_expected))

assert np.array_equal(sum_result, sum_expected)
