from math import sin
from mylib.zeros import bisect, zeros
from mylib.functions import *


def func4(value):
    return sin(value ** 4 - 3)

def func5(value):
    return value ** 9 + 2 * value ** 2 - 3 * value ** 4

def func6(value):
    return 0.2 * value ** 4 - value ** 2 + 1

epsilon = 0.000000001
links = -10
rechts = 10
print(f"Eine Nullstelle von f1 ist: {bisect(func1, -2.7, 2, epsilon)}")
print(f"Eine Nullstelle von f2 ist: {bisect(func2, -1.5, 2.5, epsilon)}")
print(f"Eine Nullstelle von f3 ist: {bisect(func3, -2.7, 2, epsilon)}")
print("--------------------")
print(f"Alle Nullstellen der f1 sind: {zeros(func1, links, rechts)}")
print(f"Alle Nullstellen der f2 sind: {zeros(func2, links, rechts)}")
print(f"Alle Nullstellen der f3 sind: {zeros(func3, links, rechts)}")
print(f"Alle Nullstellen der f4 sind: {zeros(func4, -2, 2)}")
print(f"Alle Nullstellen der f5 sind: {zeros(func5, links, rechts)}")
print(f"Alle Nullstellen der f6 sind: {zeros(func6, links, rechts)}")
