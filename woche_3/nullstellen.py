from mylib.zeros import bisect, multi_zero_finder

def func1(value):
    return -2 * value - 3

def func2(value):
    return value ** 2 - 4

def func3(value):
    return value ** 3 - 2 * value

epsilon = 0.000000001
links = -10
rechts = 10
print(f"Eine Nullstelle von f1 ist: {bisect(func1, -2.7, 2, epsilon)}")
print(f"Eine Nullstelle von f2 ist: {bisect(func2, -1.5, 2.5, epsilon)}")
print(f"Eine Nullstelle von f3 ist: {bisect(func3, -2.7, 2, epsilon)}")
print("--------------------")
print(f"Alle Nullstellen der f1 sind: {multi_zero_finder(func1, links, rechts, epsilon)}")
print(f"Alle Nullstellen der f2 sind: {multi_zero_finder(func2, links, rechts, epsilon)}")
print(f"Alle Nullstellen der f3 sind: {multi_zero_finder(func3, links, rechts, epsilon)}")