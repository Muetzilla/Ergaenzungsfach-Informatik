from mylib.functions import *
from mylib.zeros import newton, steigung
from scipy.optimize import root_scalar


function_to_find = func7
print(f"Eine Nullstelle von {function_to_find.__name__} ist:", newton(function_to_find, 1.5))

nullstellen = set([])
for i in range(-10, 11):
    if i == 0:
        continue
    print(f"Eine Nullstelle von {function_to_find.__name__} mit Startwert {i} ist:", newton(function_to_find, i))
    nullstellen.add(newton(function_to_find, i))

print(f"Alle gefundenen Nullstellen von {function_to_find.__name__} sind:", sorted(list(nullstellen)))

# print(f"Nullstellen laut scipy von {function_to_find.__name__} mit Newton sind: {root_scalar(function_to_find,x0=1.5, x1=2.5, method="newton", rtol=1e-10, maxiter=1000)}")
print(f"Nullstellen laut scipy von {function_to_find.__name__} mit Bisect sind: {root_scalar(function_to_find, bracket=[-5, 5], method="bisect")}")
# print(f"Nullstellen laut scipy von {function_to_find.__name__} mit Toms748 sind: {root_scalar(function_to_find, bracket=[-5, 5], method="toms748")}")
# print(f"Nullstellen laut scipy von {function_to_find.__name__} mit Brentq sind: {root_scalar(function_to_find, bracket=[-5, 5], method="brentq")}")

