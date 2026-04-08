import numpy as np
import matplotlib.pyplot as plt


def plot_function(
    func,
    grad,
    start_point,
    learning_rate=0.1,
    steps=50,
    x_range=(-5, 5),
    y_range=(-5, 5),
    resolution=100,
    title="Gradient Descent Visualisierung",
    show=True
):
    """
    Visualisiert eine Funktion f(x,y) + Gradient Descent Verlauf.

    Parameter:
    ----------
    func : callable
        f(x, y)

    grad : callable
        Gradient: grad(x, y) -> (df/dx, df/dy)

    start_point : tuple
        Startwert (x0, y0)

    learning_rate : float
        Schrittweite

    steps : int
        Anzahl Iterationen

    """

    # Grid erstellen
    x = np.linspace(x_range[0], x_range[1], resolution)
    y = np.linspace(y_range[0], y_range[1], resolution)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)

    # Gradient Descent berechnen
    path = [start_point]
    xk, yk = start_point

    for _ in range(steps):
        gx, gy = grad(xk, yk)
        xk = xk - learning_rate * gx
        yk = yk - learning_rate * gy
        path.append((xk, yk))

    path = np.array(path)
    Z_path = func(path[:, 0], path[:, 1])

    # Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Oberfläche mit Farbverlauf
    surf = ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.9)

    # Colorbar
    fig.colorbar(surf, ax=ax, shrink=0.6, label="Funktionswert")

    # Gradient Descent Linie
    ax.plot(
        path[:, 0],
        path[:, 1],
        Z_path,
        color="red",
        marker="o",
        label="Gradient Descent"
    )

    # Startpunkt
    ax.scatter(
        path[0, 0],
        path[0, 1],
        Z_path[0],
        color="orange",
        s=80,
        label="Startpunkt"
    )

    # Minimum (letzter Punkt)
    ax.scatter(
        path[-1, 0],
        path[-1, 1],
        Z_path[-1],
        color="blue",
        s=80,
        label="Minimum (approx.)"
    )

    # Labels
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    ax.set_title(title)

    ax.legend()

    if show:
        plt.show()

    return fig, ax