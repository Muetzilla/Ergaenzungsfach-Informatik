# Finde Mimimum mittels Gradient Descent

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


def minimize(f, x_start,  alpha = 0.01):
    max_iterations = 500
    tolerance = 1e-6
    x_new = x_start.copy()
    y_new = f(x_new)

    for iteration in range(max_iterations):
        x_old = x_new.copy()
        y_old = y_new
        grad = grad_numeric_vector(f, x_new)

        for i in range(len(x_new)):
            x_new[i] = x_old[i] - alpha * grad[i]

        y_new = f(x_new)

        if abs(y_new - y_old) < tolerance:
            print(f"Konvergiert nach {iteration + 1} Iterationen")
            break

    return x_new






