from ML.ml_lib.minimize import minimize

def f_2d(x):
    return (x[0] - 2) ** 2 + 10 * (x[1] - 4) ** 2 - 1

print("=" * 50)
print("2D Funktion: (x-2)² + 10(y-4)² - 1")
print("=" * 50)
x_start_2d = [5, -12]
result_2d = minimize(f_2d, x_start_2d)
print(f"Optimum: {result_2d}")
print(f"Funktionswert: {f_2d(result_2d):.6f}\n")


def f_3d(x):
    return (x[0] - 1) ** 2 + 2 * (x[1] - 2) ** 2 + 3 * (x[2] - 3) ** 2

print("=" * 50)
print("3D Funktion: (x-1)² + 2(y-2)² + 3(z-3)²")
print("=" * 50)
x_start_3d = [0, 0, 0]
result_3d = minimize(f_3d, x_start_3d)
print(f"Optimum: {result_3d}")
print(f"Funktionswert: {f_3d(result_3d):.6f}\n")


def f_4d(x):
    return (x[0] - 1) ** 2 + (x[1] - 2) ** 3 + (x[2] - 3) ** 2 + (x[3] - 4) ** 2

print("=" * 50)
print("4D Funktion: (x-1)² + (y-2)**3 + (z-3)² + (w-4)²")
print("=" * 50)
x_start_4d = [5, 5, 5, 5]
result_4d = minimize(f_4d, x_start_4d)
print(f"Optimum: {result_4d}")
print(f"Funktionswert: {f_4d(result_4d):.6f}\n")


def f_5d(x):
    return sum([(i + 1) * (x[i] - (i + 1)) ** 2 for i in range(5)])

print("=" * 50)
print("5D Funktion: Σ i*(x_i - i)² für i=1..5")
print("=" * 50)
x_start_5d = [0, 0, 0, 0, 0]
result_5d = minimize(f_5d, x_start_5d)
print(f"Optimum: {result_5d}")
print(f"Funktionswert: {f_5d(result_5d):.6f}\n")
