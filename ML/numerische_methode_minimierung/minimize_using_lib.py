from scipy.optimize import minimize


def f(x):
    return (x[0] - 2) ** 2 + 10 * (x[1] - 4) ** 2 - 1


start = [8.0, -3.0]
result = minimize(f, start)

print("Die Koordinaten des Optimums leigen bei: ", result.x)
print("Der Funktionswert liegt bei: ", result.fun)
print("Result: ", result)

