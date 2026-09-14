import numpy as np


def matrix_power(matrix: np.ndarray, n: int) -> np.ndarray:
	"""Return the matrix raised to the nonnegative integer power ``n``."""
	if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
		raise ValueError("matrix_power requires a square matrix")
	if n < 0:
		raise ValueError("matrix_power requires a nonnegative exponent")

	result = np.eye(matrix.shape[0], dtype=matrix.dtype)
	for _ in range(n):
		result = result @ matrix
	return result
