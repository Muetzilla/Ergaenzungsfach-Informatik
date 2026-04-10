# Gradient Descend für f(x,y) = (x-2)^2 + 10(y-4)^2 -1 mit Numerischer Ableitung
from ML.ml_lib.visualize import plot_function, draw_conturplot

def grad_numeric(x, y, h=1e-5):
    dfdx = (calc_function(x + h, y) - calc_function(x, y)) / h
    dfdy = (calc_function(x, y + h) - calc_function(x, y)) / h
    return dfdx, dfdy

def calc_function(x, y):
    return (x - 2) ** 2 + 10 * (y - 4) ** 2 - 1

alpha = 0.01
n = 500
x_start = 5
y_start = -12
x_new = x_start
y_new = y_start

# Punkte für den Plot speichern
x_values = [x_new]
y_values = [y_new]

for i in range(n):
    x_old = x_new
    y_old = y_new
    x_temp, y_temp = grad_numeric(x_old, y_old)
    x_new = x_old - alpha * x_temp
    y_new = y_old - alpha * y_temp
    print(f"Iteration {i + 1}: x={x_new:.4f}, y={y_new:.4f}")
    x_values.append(x_new)
    y_values.append(y_new)

print(f"\nMinimum bei: x = {x_new:.4f} y = {y_new:.4f}")
print(f"\nFunktionswert an Minimum:{ calc_function(x_new, y_new):.6f}")
draw_conturplot(calc_function, x_values, y_values, x_start, y_start,-10, 10)