import np


def numpy_task_4():
    n, m = map(int, input().split())

    row_matrix = np.numpy_row_matrix(n, m)

    np.numpy_print_matrix(row_matrix)


numpy_task_4()
