# Gradient Descend für f(x,y) = (x-2)^2 + 10(y-4)^2 -1
from ML.ml_lib  import *
from ML.ml_lib.visualize import plot_function


def calc_part_derivative_x(x, y):
    return 2 * (x - 2)

def calc_part_derivative_y(x, y):
    return 20 * (y - 4)

def grad_f(x, y):
    return 2 * (x - 2), 20 * (y - 4)

def calc_function(x, y):
    return (x - 2) ** 2 + 10 * (y - 4) ** 2 - 1

alpha = 0.05
n = 50
x_start = 8
y_start = -3
x_new = x_start
y_new = y_start

for i in range(n):
    x_old = x_new
    y_old = y_new

    x_new = x_old - alpha * calc_part_derivative_x(x_old, y_old)
    y_new = y_old - alpha * calc_part_derivative_y(x_old, y_old)

    print(f"Iteration {i + 1}: x={x_new:.4f}, y={y_new:.4f}")

print(f"\nMinimum bei: x = {x_new:.4f} y = {y_new:.4f}")
print(f"\nFunktionswert an Minimum:{ calc_function(x_new, y_new):.6f}")

plot_function(calc_function,start_point=(x_start, y_start), grad=grad_f(x_start, y_start), x_range=(-10, 10), y_range=(-10, 10))