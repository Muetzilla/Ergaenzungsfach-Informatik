from ML.ml_lib.visualize import draw_conturplot

def grad_numeric_vector(f, x, h=1e-5):
    gradient_list = []
    for i in range(len(x)):
        x_forward = x.copy()
        x_forward[i] += h
        x_backward = x.copy()
        x_backward[i] -= h
        dfdx = (f(x_forward) - f(x_backward)) / (2 * h)
        gradient_list.append(dfdx)
    return gradient_list


def calc_function(x):
    return (x[0] - 2) ** 2 + 10 * (x[1] - 4) ** 2 - 1


alpha = 0.05
n = 50
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
    x_temp, y_temp = grad_numeric_vector(calc_function, [x_old, y_old])
    x_new = x_old - alpha * x_temp
    y_new = y_old - alpha * y_temp
    print(f"Iteration {i + 1}: x={x_new:.4f}, y={y_new:.4f}")
    x_values.append(x_new)
    y_values.append(y_new)

print(f"\nMinimum bei: x = {x_new:.4f} y = {y_new:.4f}")
print(f"\nFunktionswert an Minimum:{calc_function(x_new, y_new):.6f}")
draw_conturplot(calc_function, x_values, y_values, x_start, y_start, -10, 10)