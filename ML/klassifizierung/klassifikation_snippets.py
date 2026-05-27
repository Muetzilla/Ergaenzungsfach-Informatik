import numpy as np
import matplotlib.pyplot as plt


# Hilfsfunktion für grafische Darstellungen
def plot_line(w, b):
    x_vals = np.linspace(-1, 8, 100)
    y_vals = -(w[0] * x_vals + b) / w[1]
    plt.plot(x_vals, y_vals)


# Hilfsfunktion für grafische Darstellungen
def plot(X, y, w, b, durchgang, step):
    plt.clf()
    plt.xlim(-1, 8)
    plt.ylim(-1, 8)

    plt.xlabel("Anzahl Ausrufezeichen")
    plt.ylabel("Länge des Betreffs")

    for X_, y_ in zip(X, y):
        color = "tab:red" if y_ < 0 else "tab:green"
        plt.scatter(X_[0], X_[1], color=color, label="Spam")

    plot_line(w, b)
    plt.grid(True)
    plt.title(f"Durchgang {durchgang}, Schritt {step + 1}, w={w}, b={b}")

    plt.draw()
    plt.pause(0.3)


# Daten
X = np.array([
    [5, 2],
    [6, 3],
    [4, 2],
    [0, 6],
    [1, 7],
    [0, 5]
])

y = np.array([1, 1, 1, -1, -1, -1])


def predict(xi, w, b):
    f = np.dot(w, xi) + b
    return +1 if f > 0 else -1


# Startwerte+
w = np.array([1.0, 1.0])
b = 0.0

durchgaenge = 3
plt.ion()
fig = plt.figure()

# Ein Durchlauf durch alle Datenpunkte
for i in range(1, durchgaenge + 1):
    for i in range(len(X)):
        xi = X[i]
        yi = y[i]

        # Linear Model
        xi * w + b
        f = np.dot(w, xi) + b

        if yi * f <= 0:
            # raise NotImplementedError("Implementieren Sie die Update-Regel")
            w = w + (yi * xi)
            b = b + yi

            print(f"Update      durch Punkt {i}:", w, b)
        else:
            print(f"Kein Update durch Punkt {i}:", w, b)
        plot(X, y, w, b, 1, i)

# switch intractive mode off
plt.ioff()
# This command blocks
plt.show()

testdaten = [(3, 2), (1,5), (4, 1)]
print(f"Vorhersage mit trainiertem Modell: w = {w}, b = {b}")
for data in testdaten:
    vorhersage = "SPAM" if predict(data, w, b) == 1 else "Kein SPAM"
    print(data, "ist", vorhersage)

