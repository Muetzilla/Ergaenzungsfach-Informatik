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

    # Plot 1: 3D Oberfläche
    fig1 = plt.figure(figsize=(10, 8))
    ax1 = fig1.add_subplot(111, projection="3d")

    # Oberfläche mit Farbverlauf
    surf = ax1.plot_surface(X, Y, Z, cmap="viridis", alpha=0.9)

    # Colorbar
    fig1.colorbar(surf, ax=ax1, shrink=0.6, label="Funktionswert")

    # Labels
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_zlabel("f(x, y)")
    ax1.set_title(title + " - 3D Oberfläche")

    # Plot 2: 2D Kontourplot mit Gradient Descent Pfad
    fig2 = plt.figure(figsize=(10, 8))
    ax2 = fig2.add_subplot(111)

    # Konturplot
    contour = ax2.contour(X, Y, Z, levels=20, cmap="viridis")
    contourf = ax2.contourf(X, Y, Z, levels=20, cmap="viridis", alpha=0.6)
    fig2.colorbar(contourf, ax=ax2, label="Funktionswert")

    # Gradient Descent Linie
    ax2.plot(
        path[:, 0],
        path[:, 1],
        color="red",
        marker="o",
        markersize=6,
        linewidth=2,
        label="Gradient Descent Pfad"
    )

    # Startpunkt
    ax2.scatter(
        path[0, 0],
        path[0, 1],
        color="orange",
        s=150,
        marker="*",
        edgecolors="black",
        linewidth=2,
        label="Startpunkt",
        zorder=5
    )

    # Minimum (letzter Punkt)
    ax2.scatter(
        path[-1, 0],
        path[-1, 1],
        color="blue",
        s=150,
        marker="*",
        edgecolors="black",
        linewidth=2,
        label="Minimum (approx.)",
        zorder=5
    )

    # Labels
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_title(title + " - 2D Gradient Descent Pfad")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    if show:
        plt.show()

    return fig1, ax1, fig2, ax2
