# task_2
def vanilla_zeros_matrix(n):
    matrix = []

    for i in range(n):
        row = [0] * n
        matrix.append(row)

    return matrix


# task_2
def vanilla_print_matrix(matrix):
    for i, row in enumerate(matrix):
        if i == 0:
            print("[", end="")
        else:
            print("\n ", end="")

        print("[" + " ".join(map(str, row)) + "]", end="")

        if i == len(matrix) - 1:
            print("]")


# task_2
def vanilla_chess_matrix(n):
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            if (i + j) % 2 == 0:
                row.append(0)
            else:
                row.append(1)

        matrix.append(row)

    return matrix


# task_4
def vanilla_row_matrix(n, m):
    matrix = []

    for i in range(n):
        if i == 0:
            row = [j for j in range(m)]
        else:
            row = [0] * m

        matrix.append(row)

    return matrix


# task_5
def vanilla_zebra_matrix(n):
    matrix = []

    for i in range(n):
        if i % 2 == 0:
            row = [1] * n
        else:
            row = [0] * n

        matrix.append(row)

    return matrix


# task_8
def vanilla_count_zeros_and_non_zeros(array):
    zero_count = 0
    non_zero_count = 0

    for number in array:
        if number == 0:
            zero_count += 1
        else:
            non_zero_count += 1

    return zero_count, non_zero_count


# task_9
def vanilla_reversed_range(n):
    reversed_range = list(range(n, -1, -1))

    return reversed_range


# task_9
def vanilla_print_array(array):
    print("[" + " ".join(map(str, array)) + "]")


# task_12
def vanilla_frame_matrix(n):
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                row.append(0.0)
            else:
                row.append(1.0)

        matrix.append(row)

    return matrix


# task_13
def vanilla_8x8_chess_matrix():
    matrix = []

    for i in range(8):
        if i % 2 == 0:
            row = [0, 1] * 4
        else:
            row = [1, 0] * 4

        matrix.append(row)

    return matrix


# task_15
def vanilla_striped_matrix(n):
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            if j % 2 == 0:
                row.append(0)
            else:
                row.append(1)

        matrix.append(row)

    return matrix


# task_19
def vanilla_evenly_spaced_array(n):
    array = [round(0.0 + i * (1.0 - 0.0) / (n + 1), 3) for i in range(1, n + 1)]

    return array
