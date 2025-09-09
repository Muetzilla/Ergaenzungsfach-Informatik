from mylib.zeros import zeros

def func(value):
    return 0.2 * value ** 4 - value ** 2 + 1

def steigung(x, dx = 0.000001):
    dy = func(x + dx/2) - func(x - dx/2)
    return dy / dx

print(zeros(steigung, -10, 10))