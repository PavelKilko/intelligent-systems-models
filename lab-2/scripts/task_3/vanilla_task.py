import vanilla


def vanilla_task():
     a = [[5, 1, 7],
          [-10, -2, 1],
          [0, 1, 2]]

     b = [[2, 4, 1],
          [3, 1, 0],
          [7, 2, 1]]

     c1 = vanilla.subtract_matrices(a, b)
     c2 = vanilla.multiply_matrices(a, a)
     c3 = vanilla.add_matrices(c2, b)
     c4 = vanilla.multiply_matrices(c1, c3)
     result = vanilla.multiply_matrix_by_scalar(c4, 2)

     print(result)


vanilla_task()
