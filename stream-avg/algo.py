import numpy as np

data = np.random.normal(loc=0, scale=10, size=100)
print(f'mean = {np.mean(data):.6f}')

print('method 1: mean = ((i-1)*mean+x)/i')
mean = 0
for i, x in enumerate(data, 1):
    mean = ((i-1)*mean + x) / i
print(f'=> mean = {mean:.6f}')

print('method 2: mean = m*mean+n*x; m = 1/(2-m); n = n/(n+1)')
mean, m, n = 0, 0, 1
for x in data:
    mean = m*mean + n*x
    m, n = 1/(2-m), n/(n+1)
print(f'=> mean = {mean:.6f}')