import numpy as np
from scipy.optimize import minimize

def f1(x, theta):
    return theta[0] + theta[1] * x


def f2(x, theta):
    a, b, c = theta[0], theta[1], theta[2]
    return a * x**2 + b * x + c


def f3(x, theta, tenv=23):
    a, tau = theta[0], theta[1]
    return tenv + a * np.exp(-x/tau)

def f4(x, theta):
    a, b, c, d, e = theta[0], theta[1], theta[2], theta[3], theta[4]
    return a * x**4 + b * x**3 + c * x**2 + d * x + e

def f5(x, theta):
    a, tau, tenv = theta[0], theta[1], theta[2]
    return tenv + a * np.exp(-x/tau)



def loss_function_factory(model, data, loss):

    def loss_function(theta):
        return loss(theta, model, data)

    return loss_function


def loss1(params, model, data):
    time_values, temp_values = data
    modellwert = model(time_values, params)
    loss = np.sum(abs(temp_values - modellwert))
    return loss


def loss2(params, model, data):
    time_values, temp_values = data
    modellwert = model(time_values, params)
    loss = np.sum((temp_values - modellwert) ** 2)
    return loss



time_values = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
temp_values = np.array([84.0, 78.5, 75.7, 70.5, 67.3, 63.1, 61.1, 58.1, 54.0, 52.3])

#Anfangsparameter definieren
a = 60.0
tau = 3.0
tenv = 25

x_start_5 = np.array([a, tau, tenv])
x_start_4 = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
x_start_3 = np.array([a, tau])
x_start_2 = np.array([1.0, 1.0, 1.0])
x_start_1 = np.array([1.0, 1.0])

#Auswählen, welche Funktion optimiert werden soll
x_start = x_start_3

models = [f1, f2, f3, f4, f5]
model_names = ["Lineares Modell", "Quadratisches Modell", "Exponentielles Modell", "Polynom 4. Grades", "Exponentielles Modell mit variablem tenv"]
model_start_params = [x_start_1, x_start_2, x_start_3, x_start_4, x_start_5]
loss_values = []

for model, name, startparams in zip(models, model_names, model_start_params):
    loss_function = loss_function_factory(model, (time_values, temp_values), loss2)
    result = minimize(loss_function, startparams)
    print(f"\n{name}:")
    print("Optimierte Parameter:", result.x)
    print("Finale Loss:", loss_function(result.x))
    loss_values.append((name, loss_function(result.x)))


best_model = min(loss_values, key=lambda x: x[1])
print(f"\nBestes Modell: {best_model[0]} mit Loss: {best_model[1]:.4f}")
