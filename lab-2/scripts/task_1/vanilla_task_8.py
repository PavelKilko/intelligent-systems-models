import vanilla
import random

def vanilla_task_8():
    array = list((map(int, input().split())))

    zero_count, non_zero_count = vanilla.vanilla_count_zeros_and_non_zeros(array)

    print("Нулів:", zero_count)
    print("Не нулів:", non_zero_count)


def vanilla_task_8_rand():
    n = int(input())

    array = [random.randint(0, 100) for _ in range(n)]

    zero_count, non_zero_count = vanilla.vanilla_count_zeros_and_non_zeros(array)

    print("Нулів:", zero_count)
    print("Не нулів:", non_zero_count)


vanilla_task_8()
vanilla_task_8_rand()
