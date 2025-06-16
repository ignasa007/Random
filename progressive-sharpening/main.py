from math import atan
import numpy as np
import matplotlib.pyplot as plt


@np.vectorize
def f(x, shift, scale):
    return scale * atan(x-shift)**2

@np.vectorize
def df(x, shift, scale):
    return scale * (2*(x-shift)) / ((x-shift)**4+1)

@np.vectorize
def d2f(x, shift, scale):
    return scale * (2-6*(x-shift)**4) / ((x-shift)**4+1)**2

###

def params1():
    shift, scale = 3., 10.
    return shift, scale

def f1(x):
    shift, scale = params1()
    return f(x, shift, scale)

def df1(x):
    shift, scale = params1()
    return df(x, shift, scale)

def d2f1(x):
    shift, scale = params1()
    return d2f(x, shift, scale)

###

def params2():
    shift, scale = 3.5, 150.
    return shift, scale

def f2(x):
    shift, scale = params2()
    return f(x, shift, scale)

def df2(x):
    shift, scale = params2()
    return df(x, shift, scale)

def d2f2(x):
    shift, scale = params2()
    return d2f(x, shift, scale)

###

@np.vectorize
def g(x):
    return min(f1(x), f2(x))

@np.vectorize
def dg(x):
    return np.where(f1(x) < f2(x), df1(x), df2(x))

@np.vectorize
def d2g(x):
    return np.where(f1(x) < f2(x), d2f1(x), d2f2(x))

###

xs = np.linspace(3.1, 3.9, 1000)

iterates = [3.82]
for _ in range(5):
    iterates.append(iterates[-1] - 0.015 * dg(iterates[-1]))

plt.plot(xs, g(xs), color='blue')
plt.plot(iterates, g(iterates), color='red', marker='o', linestyle='--', label='Trajectory')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid()
plt.legend()
plt.savefig('trajectory.png')
plt.close()

plt.plot(xs, d2g(xs), color='blue')
plt.plot(iterates, d2g(iterates), color='red', marker='o', linestyle='--', label='Trajectory')
plt.hlines(2/0.015, xmin=3.1, xmax=3.9, color='black', linestyle='--', label=r'$2/\eta$')
plt.xlabel(r'$x$')
plt.ylabel(r'$d^2f/dx^2$')
plt.grid()
plt.legend()
plt.savefig('sharpness.png')
plt.close()