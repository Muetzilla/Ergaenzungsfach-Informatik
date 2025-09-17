from mylib.functions import *
from mylib.zeros import steigung


def newton(f, x_0, delta = 1e-5, epsilon = 1e-5):
    """
    :param f: Die Funktion einer Variable
    :param x_0: Den Startwert der Suche
    :param epsilon:
    :param delta:
    :return: Die x Koordinate einer Nullstelle der Funktion f
    """
    xn = x_0
    max_iterations = 1000

    for i in range(max_iterations):
        xn_minus_1 = xn
        xn = xn - f(xn) / steigung(f, xn)
        # print(xn)
        if abs(xn - xn_minus_1) <= delta or abs(f(xn)) <= epsilon:
            break

    return round(xn,5)

function_to_find = funcSPAMM2
print(f"Eine Nullstelle von {function_to_find.__name__} ist:", newton(function_to_find, 1))

nullstellen = set([])
for i in range(-10, 11):
    if i == 0:
        continue
    print(f"Eine Nullstelle von {function_to_find.__name__} mit Startwert {i} ist:", newton(function_to_find, i))
    nullstellen.add(newton(function_to_find, i))

print(f"Alle gefundenen Nullstellen von {function_to_find.__name__} sind:", sorted(list(nullstellen)))


