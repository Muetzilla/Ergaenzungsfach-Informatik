from ML.ml_lib.minimize import minimize
def f(x):
    return (x[0] - 2) ** 2 + 10 * (x[1] - 4) ** 2 - 1

x_start = [5, -12]
result = minimize(f, x_start)
print(f"Optimum: {result}")
print(f"Funktionswert: {f(result):.6f}\n")
