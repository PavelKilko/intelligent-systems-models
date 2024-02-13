import vanilla


def vanilla_task_4():
    n, m = map(int, input().split())

    row_matrix = vanilla.vanilla_row_matrix(n, m)

    vanilla.vanilla_print_matrix(row_matrix)


vanilla_task_4()