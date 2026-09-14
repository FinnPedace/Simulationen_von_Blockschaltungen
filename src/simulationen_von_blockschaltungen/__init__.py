import numpy as np


def hello() -> str:
    return "Hello from simulationen-von-blockschaltungen!"


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    """Return the matrix product in the order given."""
    if not matrices:
        raise ValueError("matrix_product requires at least one matrix")

    result = matrices[0]
    for matrix in matrices[1:]:
        result = result @ matrix
    return result
