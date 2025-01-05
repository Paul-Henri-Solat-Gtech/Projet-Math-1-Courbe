import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import numpy as np
import math
import random

# Hermite function
def Hermite(x, ListX, ListY, y_derived):
    xi = ListX[0]
    xii = ListX[1]
        
    th = ((x - xi)/(xii - xi))
     
    h1 = 2*th**3 - 3*th**2+1
    h2 = -2*th**3+3*th**2
    h3 = th**3-2*th**2+th
    h4 = th**3-th**2
    result = ListY[0]*h1 + ListY[1]*h2 + y_derived[0]*h3 + y_derived[1]*h4
    return result

# Plot Hermite curve
def PlayerCurve(ax, ListX, ListY, y_derived):
    x_vals = np.linspace(ListX[0], ListX[1], 100)
    y_vals = [Hermite(x, ListX, ListY, y_derived) for x in x_vals]
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
                PlayerCurve(ax, ListX, ListY, y_derived)
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

#-------------------------------------------------------

# Random numbers
def RandomInt(min, max):
    randNb = random.randint(min, max)
    return(randNb)
def RandomFloat(min, max):
    randNb = random.uniform(min, max)
    return round(randNb, 1)

# plotCurve
def PlotCurve(ListPosX, ListPosY, ListPosY_derived):
    n=len(ListPosX)
    for i in range(n-1):
        x_points = [ListPosX[i],ListPosX[i+1]]
        y_points = [ListPosY[i],ListPosY[i+1]]
        y_derived = [ListPosY_derived[i],ListPosY_derived[i+1]]
    
        # Generer les valeurs de x pour dessiner le polynome
        x_vals = np.linspace(ListPosX[i], ListPosX[i+1], 400)

        # Calculer les valeurs de y pour ces x en utilisant le polynome de Lagrange
        y_vals = [Hermite(x, x_points, y_points, y_derived) for x in x_vals]

        # Tracer le polynome de Lagrange et les points de donnees
        plt.plot(x_vals, y_vals, label=f'Segment {i + 1}', color='black')


def Shape(xA,yA,yyA,xB,yB,yyB,xC,yC,yyC,xD,yD,yyD):    
        
        # A - B - C - D
        ListX = [xA, xB, xC, xD, xA]
        ListY = [yA, yB, yC, yD, yA]
        ListY_derived = [yyA, yyB, yyC, yyD,yyA]
        PlotCurve(ListX, ListY, ListY_derived)

def DrawRandShape():
    listPoints = []
    listCoef = []

    while len(listCoef) < 5 :
        newCoef = RandomFloat(-5,5)
        listCoef.append(newCoef)

    while len(listPoints) < 5:
        newX = RandomInt(-10,10)

        while newX in [point[0] for point in listPoints]:
            newX = RandomInt(-10,10)

        newY = RandomInt(-10,10)

        listPoints.append((newX, newY))
    Shape(listPoints[0][0],listPoints[0][1],listCoef[0],listPoints[1][0],listPoints[1][1],listCoef[1],listPoints[2][0],listPoints[2][1],listCoef[2],listPoints[3][0],listPoints[3][1],listCoef[3])
    
    print("coefs:", listCoef)
    print("points:", listPoints)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Random Shape')
    plt.grid(True)

    ax = plt.gca()
    ax.set_aspect('equal', adjustable='datalim')

    # Definir un pas de 1 pour les graduations
    x_min, x_max = ax.get_xlim()  # Obtenir les limites de l'axe x
    y_min, y_max = ax.get_ylim()  # Obtenir les limites de l'axe y

    ax.set_xticks(np.arange(math.floor(x_min), math.ceil(x_max) + 1, 2))  # Pas de 1 en x
    ax.set_yticks(np.arange(math.floor(y_min), math.ceil(y_max) + 1, 2))  # Pas de 1 en y
    plt.show()

# Random curve
DrawRandShape()

# Execute the interactive trace
TraceInteractive()