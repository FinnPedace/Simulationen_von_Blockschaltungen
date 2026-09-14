import numpy as np


def matrix_sum(matrices: list[np.ndarray]) -> np.ndarray:
    """Return the element-wise sum of matrices with the same shape."""
    if not matrices:
        raise ValueError("matrix_sum requires at least one matrix")

    expected_shape = matrices[0].shape
    if any(matrix.shape != expected_shape for matrix in matrices[1:]):
        raise ValueError("all matrices must have the same shape")

    result = matrices[0].copy()
    for matrix in matrices[1:]:
        result += matrix
    return result
