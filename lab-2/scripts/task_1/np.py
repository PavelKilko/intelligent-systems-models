import numpy as np


# task_2
def numpy_chess_matrix(n):
    matrix = np.ones((n, n), dtype=int)

    matrix[::2, ::2] = 0
    matrix[1::2, 1::2] = 0

    return matrix


# task_2
def numpy_print_matrix(matrix):
    print(matrix)


# task_4
def numpy_row_matrix(n, m):
    matrix = np.zeros((n, m), dtype=int)

    matrix[0] = np.arange(m)

    return matrix


# task_5
def numpy_zebra_matrix(n):
    matrix = np.zeros((n, n), dtype=int)

    matrix[::2, :] = 1

    return matrix


# task_8
def numpy_count_zeros_and_non_zeros(array):
    array = np.array(array)

    zero_count = np.sum(array == 0)
    non_zero_count = np.sum(array != 0)

    return zero_count, non_zero_count


# task_9
def numpy_reversed_range(n):
    reversed_range = np.arange(n, -1, -1)

    return reversed_range


# task_9
def numpy_print_array(array):
    print(array)


# task_12
def numpy_frame_matrix(n):
    matrix = np.ones((n, n), dtype=float)

    matrix[0, :] = 0.
    matrix[-1, :] = 0.

    matrix[:, 0] = 0.
    matrix[:, -1] = 0.

    return matrix


# task_13
def numpy_8x8_chess_matrix():
    matrix = np.zeros((8, 8), dtype=int)

    matrix[::2, 1::2] = 1
    matrix[1::2, ::2] = 1

    return matrix


# task_15
def numpy_striped_matrix(n):
    matrix = np.zeros((n, n), dtype=int)

    matrix[:, 1::2] = 1

    return matrix


# task_19
def numpy_evenly_spaced_array(n):
    array = np.linspace(0.0, 1.0, n + 1, endpoint=False)[1:]

    array = np.around(array, decimals=3)

    return array
