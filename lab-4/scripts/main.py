import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid')

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y)
plt.plot(x, z)

plt.show()