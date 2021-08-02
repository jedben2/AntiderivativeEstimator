# Antiderivative Estimator
# Using taylor polynomials
# More detail in README.md

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import math
import time

# Plot area and detail
X_LOWER = -10
X_UPPER = 10
Y_LOWER = -10
Y_UPPER = 10
SPACING = 1000

# Set up graph
plt.style.use('bmh')
fig, ax = plt.subplots()
plt.title("Antiderivative Approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim([X_LOWER, X_UPPER])
plt.ylim([Y_LOWER, Y_UPPER])

# Increase degree of accuracy
ACCURACY = 100
C = -3

# Does the function plot or not?
NO_f = 0
NO_F = 0

# Set up x axis
x = np.linspace(X_LOWER, X_UPPER, SPACING)


# Removes a function from plot if not needed without breaking code
def zero():
    return [0 for _ in range(len(x))]


# f(x). put whatever you like in here as long as it can return a real number
def f(x):
    return log(cos(x) ** 2)


# Version of f(x) which will be able to be plotted onto the graph. Can differ from the one above
def f_plot(x):
    return 2 * np.log(np.power(np.cos(x), 2))


# Antiderivative function. Works as explained in README.md
def F(X):
    F = 0
    x = symbols('x')
    for n in range(ACCURACY):
        F += lambdify(x, diff(f(x), x, n))(C) / math.factorial(n + 1) * np.power(X - C, n + 1)
    return F


# Set up y axis for both functions. replace either one with the zero() function if want to get rid
print("Start estimation")
y1 = y2 = zero()
if not NO_f: y1 = f_plot(x)
t1 = time.time()
if not NO_F: y2 = F(x)
print(f"Time taken: {time.time() - t1} seconds")

# Plot the points and show the graph
ax.plot([-1000, 1000], [0, 0], color='black', linewidth=3)
ax.plot([0, 0], [-1000, 1000], color='black', linewidth=3)

if not y1 is zero(): ax.plot(x, y1, label='f(x)')
ax.plot(x, y2, label='F(x)')
ax.legend()
plt.show()
