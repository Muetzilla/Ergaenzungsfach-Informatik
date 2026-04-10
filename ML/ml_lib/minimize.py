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


def minimize(f, x_start):
    #Abbruchbedingungen
    max_iterations = 100
    tolerance = 1e-6

    y_start = f(x_start)
    alpha = 0.01
    value_history = [(x_start, y_start)]
    x_new, y_new = x_start, y_start



