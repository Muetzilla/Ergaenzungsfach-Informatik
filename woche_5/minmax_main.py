import math
from mylib.minmax import minmax, minmax2
from mylib.zeros import maxima, minima
from mylib.functions import func4, func5

# def func1(value):
#     return 0.2 * value ** 4 - value ** 2 + 1
#
# def func2(value):
#     return 3 * value ** 2 * math.e ** -value

print(f"Die Funktion {func4.__name__} hat folgende Extremwertpunkte: {minmax2(func4, -10, 10)}")
print(f"Die Funktion {func5.__name__} hat folgende Extremwertpunkte: {minmax2(func5, -10, 10)}")

print(f"Die Funktion {func4.__name__} hat folgende Maximalwerte: {maxima(func4, -10, 10)}")
print(f"Die Funktion {func4.__name__} hat folgende Minimalwerte: {minima(func4, -10, 10)}")
