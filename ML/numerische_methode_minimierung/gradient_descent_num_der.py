# Gradient Descend für f(x,y) = (x-2)^2 + 10(y-4)^2 -1 mit Numerischer Ableitung
from ML.ml_lib  import *
from ML.ml_lib.visualize import plot_function


def grad_numeric(x, y, h=1e-5):
    dfdx = (calc_function(x + h, y) - calc_function(x - h, y)) / h
    dfdy = (calc_function(x + h, y) - calc_function(x - h, y)) / h
    return dfdx, dfdy

def calc_function(x, y):
    return (x - 2) ** 2 + 10 * (y - 4) ** 2 - 1

alpha = 0.01
n = 500
x_start = 8
y_start = -3
x_new = x_start
y_new = y_start

for i in range(n):
    x_old = x_new
    y_old = y_new
    x_new, y_new = grad_numeric(x_old, y_old)
    print(f"Iteration {i + 1}: x={x_new:.4f}, y={y_new:.4f}")

print(f"\nMinimum bei: x = {x_new:.4f} y = {y_new:.4f}")
print(f"\nFunktionswert an Minimum:{ calc_function(x_new, y_new):.6f}")

