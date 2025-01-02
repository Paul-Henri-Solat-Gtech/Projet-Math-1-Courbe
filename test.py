import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import numpy as np

# Hermite function
def hermite(x, ListX, ListY, y_derived):
    xi = ListX[0]
    xii = ListX[1]
    th = (x - xi) / (xii - xi)
    h1 = 2 * th**3 - 3 * th**2 + 1
    h2 = -2 * th**3 + 3 * th**2
    h3 = th**3 - 2 * th**2 + th
    h4 = th**3 - th**2
    return ListY[0] * h1 + ListY[1] * h2 + y_derived[0] * h3 + y_derived[1] * h4

# Plot Hermite curve
def plotCurve(ax, ListX, ListY, y_derived):
    x_vals = np.linspace(ListX[0], ListX[1], 100)
    y_vals = [hermite(x, ListX, ListY, y_derived) for x in x_vals]
    ax.plot(x_vals, y_vals, 'b')

# Interactive point insertion
def TraceInteractive():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_axes([0.1, 0.4, 0.8, 0.55])  # Zone de tracé principale
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title("Polynome d'Hermite - Points Interactifs")
    ax.grid(True)

    points = []

    # Mise à jour de la courbe
    def update_plot(event):
        ax.cla()
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title("Polynome d'Hermite - Points Interactifs")
        ax.grid(True)
        if len(points) >= 2:
            for i in range(len(points) - 1):
                ListX = [points[i][0], points[i + 1][0]]
                ListY = [points[i][1], points[i + 1][1]]
                y_derived = [0, 0]  # Par défaut, dérivée nulle
                plotCurve(ax, ListX, ListY, y_derived)
        plt.draw()

    # Ajouter un point
    def add_point(event):
        if len(points) < 5:
            try:
                x_val = float(x_input.text)
                y_val = float(y_input.text)
                points.append((x_val, y_val))
                ax.plot(x_val, y_val, 'ro')  # Point rouge pour chaque point ajouté
                plt.draw()
            except ValueError:
                print("Entrées non valides. Veuillez entrer des nombres.")

    # Effacer tous les points
    def clear_points(event):
        points.clear()
        ax.cla()
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title("Polynome d'Hermite - Points Interactifs")
        ax.grid(True)
        plt.draw()

    # Widgets
    axbox_x = fig.add_axes([0.1, 0.25, 0.3, 0.05])  # Zone de saisie pour X
    x_input = TextBox(axbox_x, 'X:', initial="0")

    axbox_y = fig.add_axes([0.5, 0.25, 0.3, 0.05])  # Zone de saisie pour Y
    y_input = TextBox(axbox_y, 'Y:', initial="0")

    add_ax = fig.add_axes([0.1, 0.1, 0.2, 0.075])  # Bouton pour ajouter un point
    add_button = Button(add_ax, 'Add Point')
    add_button.on_clicked(add_point)

    update_ax = fig.add_axes([0.4, 0.1, 0.2, 0.075])  # Bouton pour mettre à jour
    update_button = Button(update_ax, 'Update')
    update_button.on_clicked(update_plot)

    clear_ax = fig.add_axes([0.7, 0.1, 0.2, 0.075])  # Bouton pour effacer
    clear_button = Button(clear_ax, 'Clear')
    clear_button.on_clicked(clear_points)

    plt.show()

# Execute the interactive trace
TraceInteractive()
