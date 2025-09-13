import matplotlib
# matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from mylib.zeros import steigung, minmax, maxima, minima
from mylib.functions import *

func = func2
left_boundary = -3
right_boundary = 3
accuracy = 4
x = np.linspace(left_boundary, right_boundary, 1500)
y_f = [func(v) for v in x]
y_steigung = steigung(func, x)
minima_values = minima(func, left_boundary, right_boundary)
maxima_values = maxima(func, left_boundary, right_boundary)
# Plot
plt.figure(figsize=(12,9))
plt.plot(x, y_f, color="blue",label=f"f(x) = {func.__doc__}")
plt.plot(x, y_steigung, color="red", label="f'(x)")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
# Plot min/max points
for i in range(len(minima_values)):
    plt.plot(minima_values[i], func(minima_values[i]), 'go', label=f"Minima ({round(minima_values[i],accuracy)} | {round(func(minima_values[i]),accuracy)})")
    plt.annotate("Minima", (minima_values[i], func(minima_values[i])), textcoords="offset points", xytext=(0,-15), ha='center', color='green')
for i in range(len(maxima_values)):
    plt.plot(maxima_values[i], func(maxima_values[i]), 'go', label=f"Maxima ({round(maxima_values[i], accuracy)} | {round(func(maxima_values[i]),accuracy)})")
    plt.annotate("Maxima", (maxima_values[i], func(maxima_values[i])), textcoords="offset points", xytext=(0,-15), ha='center', color='green')
# Labels and legend
plt.title(f"Graph der Funktion {func.__name__}, Ableitung und Extremstellen")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()