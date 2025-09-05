from math import sin
from mylib.zeros import bisect, zeros

def func1(value):
    return -2 * value - 3

def func2(value):
    return value ** 2 - 4

def func3(value):
    return value ** 3 - 2 * value

def func4(value):
    return sin(value ** 4 - 3)

def func5(value):
    return value ** 9 + 2 * value ** 2 - 3 * value ** 4

def func6(value):
    return 0.2 * value ** 4 - value ** 2 + 1

epsilon = 0.000000001
links = -10
rechts = 10
delta = (abs(links) + rechts) / 1000
print(f"Eine Nullstelle von f1 ist: {bisect(func1, -2.7, 2, epsilon)}")
print(f"Eine Nullstelle von f2 ist: {bisect(func2, -1.5, 2.5, epsilon)}")
print(f"Eine Nullstelle von f3 ist: {bisect(func3, -2.7, 2, epsilon)}")
print("--------------------")
print(f"Alle Nullstellen der f1 sind: {zeros(func1, links, rechts,delta ,epsilon)}")
print(f"Alle Nullstellen der f2 sind: {zeros(func2, links, rechts,delta, epsilon)}")
print(f"Alle Nullstellen der f3 sind: {zeros(func3, links, rechts,delta, epsilon)}")
print(f"Alle Nullstellen der f4 sind: {zeros(func4, -2, 2, delta, epsilon)}")
print(f"Alle Nullstellen der f5 sind: {zeros(func5, links, rechts, delta, epsilon)}")
print(f"Alle Nullstellen der f6 sind: {zeros(func6, links, rechts, delta, epsilon)}")
