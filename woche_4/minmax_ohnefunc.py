from mylib.zeros import zeros
from mylib.functions import func4


def steigung(x, dx = 0.000001):
    dy = func4(x + dx/2) - func4(x - dx/2)
    return dy / dx

print(zeros(steigung, -10, 10))