import numpy as np


def numpy_task():
    a = np.array([
        [5, 1, 7],
        [-10, -2, 1],
        [0, 1, 2]
    ])

    b = np.array([
        [2, 4, 1],
        [3, 1, 0],
        [7, 2, 1]
    ])

    result = 2 * (a - b) @ (a @ a + b)

    print(result)


numpy_task()
