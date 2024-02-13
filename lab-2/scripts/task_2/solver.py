import numpy as np
import cramer

a = np.array([
    [1, 2, 3, 4],
    [2, 1, 2, 3],
    [3, 2, 1, 2],
    [4, 3, 2, 1]
])

b = np.array([5, 1, 1, -5])

solution = cramer.cramer4x4(a, b)

print(solution)

print(np.allclose(a @ solution, b))

print(np.allclose(np.linalg.inv(a) @ b, solution))

print(np.allclose(np.linalg.solve(a, b), solution))

