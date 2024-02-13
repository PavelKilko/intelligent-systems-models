import np
import random


def numpy_task_8():
    array = list((map(int, input().split())))

    zero_count, non_zero_count = np.numpy_count_zeros_and_non_zeros(array)

    print("Нулів:", zero_count)
    print("Не нулів:", non_zero_count)


def numpy_task_8_rand():
    n = int(input())

    array = [random.randint(0, 100) for _ in range(n)]

    zero_count, non_zero_count = np.numpy_count_zeros_and_non_zeros(array)

    print("Нулів:", zero_count)
    print("Не нулів:", non_zero_count)


numpy_task_8()
numpy_task_8_rand()
