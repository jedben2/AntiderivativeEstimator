# Antiderivative Estimator
# Using maclaurin series
# More detail in README.md

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import math
import time

plt.style.use('bmh')
fig, ax = plt.subplots()

# Plot area and detail
X_LOWER = -10
X_UPPER = 10
Y_LOWER = -10
Y_UPPER = 10
SPACING = 200
plt.xlim([X_LOWER, X_UPPER])
plt.ylim([Y_LOWER, Y_UPPER])

# Antiderivative series
ITER = 20
C = 0

# Plot decider
NO_f = 0
NO_F = 0

# Set up x axis
x = np.linspace(X_LOWER, X_UPPER, SPACING)


# Removes a function from plot if not needed without breaking code
def zero():
    return [0 for _ in range(len(x))]


# f(x). put whatever you like in here as long as it can return a real number
def f(x):
    return abs(x)


def f_plot(x):
    return abs(x)


# Antiderivative function. Works as explained in README.md
def F(X):
    F = 0
    x = symbols('x')
    for n in range(ITER):
        F += lambdify(x, diff(f(x), x, n))(C) / math.factorial(n + 1) * np.power(X - C, n + 1)
    return F


# Set up y axis for both functions. replace either one with the zero() function if want to get rid
y1 = y2 = zero()
if not NO_f: y1 = f_plot(x)
t1 = time.time()
if not NO_F: y2 = F(x)
print(f"Time taken: {t1 - time.time()} seconds")

# Plot the points and show the graph
ax.plot([-1000, 1000], [0, 0], color='black', linewidth=3)
ax.plot([0, 0], [-1000, 1000], color='black', linewidth=3)

if not max(y1) == 0 and not min(y1) == 0: ax.plot(x, y1, label='f(x)')
ax.plot(x, y2, label='F(x)')
ax.legend()
plt.show()
