import numpy as np


def pauli_x() -> np.ndarray:
    """Return the Pauli-X matrix."""
    return np.array([[0, 1], [1, 0]], dtype=complex)


def pauli_y() -> np.ndarray:
    """Return the Pauli-Y matrix."""
    return np.array([[0, -1j], [1j, 0]], dtype=complex)


def pauli_z() -> np.ndarray:
    """Return the Pauli-Z matrix."""
    return np.array([[1, 0], [0, -1]], dtype=complex)
