import numpy as np


def cramer4x4(a, b):
    mask = np.broadcast_to(np.diag([1, 1, 1, 1]), [4, 4, 4]).swapaxes(0, 1)
    Ms = np.where(mask, np.repeat(b, 4).reshape(4, 4), a)
    return np.linalg.det(Ms) / np.linalg.det(a)
