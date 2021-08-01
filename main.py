# Antiderivative Estimator
# Using maclaurin series
# More detail in README.md

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from math import factorial

plt.style.use('bmh')
fig, ax = plt.subplots()

BOUND_LOWER = -1
BOUND_UPPER = 4
SPACING = 50
ITER = 100

x = np.linspace(BOUND_LOWER, BOUND_UPPER, SPACING)


def f(x):
    return sin(x ** 2)


def F(X):
    F = 0
    x = symbols('x')
    for n in range(ITER):
        derivative = lambdify(x, diff(f(x), x, n))
        F += derivative(0) / factorial(n + 1) * np.power(X, n + 1)
    return F


y = F(x)

print(list(zip(x, y)))

ax.plot(x, y, label='F(x)')
ax.legend()
plt.show()
