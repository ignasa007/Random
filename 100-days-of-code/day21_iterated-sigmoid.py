import numpy as np
import matplotlib.pyplot as plt

sigmoid = lambda x: 1 / (1 + np.exp(-x))
x_lim, steps, num_times = 8, 5, 2

data = [np.linspace(-x_lim, x_lim, 1000)]
for _ in range(10):
    x = data[-1]
    x = x_lim * (2*(x-np.min(x))/(np.max(x)-np.min(x)) - 1)
    data.append(sigmoid(x))
x, *data = data

indices = list(range(steps)) + list(range(steps-1, -1, -1))

for i in indices*num_times:
    plt.clf()
    plt.title(f'Sigmoid, iter={i}')
    plt.scatter(x, data[i], s=15)
    plt.grid()
    plt.pause(0.5)
plt.show()