def subtract_matrices(matrix_l, matrix_r):
    if len(matrix_l) != len(matrix_r) or len(matrix_l[0]) != len(matrix_r[0]):
        raise ValueError("Матриці мають різну розмірність")

    result = []
    for i in range(len(matrix_l)):
        row = []
        for j in range(len(matrix_l[0])):
            row.append(matrix_l[i][j] - matrix_r[i][j])
        result.append(row)

    return result


def add_matrices(matrix_l, matrix_r):
    if len(matrix_l) != len(matrix_r) or len(matrix_l[0]) != len(matrix_r[0]):
        raise ValueError("Матриці мають різну розмірність")

    result = []
    for i in range(len(matrix_l)):
        row = []
        for j in range(len(matrix_l[0])):
            row.append(matrix_l[i][j] + matrix_r[i][j])
        result.append(row)

    return result


def multiply_matrices(matrix_l, matrix_r):
    if len(matrix_l[0]) != len(matrix_r):
        raise ValueError("Неправильні розміри матриць для множення")

    result = [[0 for _ in range(len(matrix_r[0]))] for _ in range(len(matrix_l))]

    for i in range(len(matrix_l)):
        for j in range(len(matrix_r[0])):
            for k in range(len(matrix_r)):
                result[i][j] += matrix_l[i][k] * matrix_r[k][j]

    return result


def multiply_matrix_by_scalar(matrix, scalar):
    result = []

    for row in matrix:
        new_row = [scalar * element for element in row]
        result.append(new_row)

    return result
