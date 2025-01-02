import numpy as np
import matplotlib.pyplot as plt
import math
import random
from math import*

def randomInt(min, max):
    randNb = random.randint(min, max)
    return(randNb)

def randomFloat(min, max):
    randNb = random.uniform(min, max)
    return round(randNb, 1)

def hermite(x, ListX, ListY, y_derived):
    xi = ListX[0]
    xii = ListX[1]
        
    th = ((x - xi)/(xii - xi))
     
    h1 = 2*th**3 - 3*th**2+1
    h2 = -2*th**3+3*th**2
    h3 = th**3-2*th**2+th
    h4 = th**3-th**2
    result = ListY[0]*h1 + ListY[1]*h2 + y_derived[0]*h3 + y_derived[1]*h4
    return result

def plotCurve(ListPosX, ListPosY, ListPosY_derived):
    n=len(ListPosX)
    for i in range(n-1):
        x_points = [ListPosX[i],ListPosX[i+1]]
        y_points = [ListPosY[i],ListPosY[i+1]]
        y_derived = [ListPosY_derived[i],ListPosY_derived[i+1]]
    
        # Generer les valeurs de x pour dessiner le polynome
        x_vals = np.linspace(ListPosX[i], ListPosX[i+1], 400)

        # Calculer les valeurs de y pour ces x en utilisant le polynome de Lagrange
        y_vals = [hermite(x, x_points, y_points, y_derived) for x in x_vals]

        # Tracer le polynome de Lagrange et les points de donnees
        plt.plot(x_vals, y_vals, label=f'Segment {i + 1}', color='black')

def Shape(xA,yA,yyA,xB,yB,yyB,xC,yC,yyC,xD,yD,yyD):    
        
        # A - B - C - D
        ListX = [xA, xB, xC, xD, xA]
        ListY = [yA, yB, yC, yD, yA]
        ListY_derived = [yyA, yyB, yyC, yyD,yyA]
        plotCurve(ListX, ListY, ListY_derived)

def DrawRandShape():
    listPoints = []
    listCoef = []

    while len(listCoef) < 5 :
        newCoef = randomFloat(-5,5)
        listCoef.append(newCoef)

    while len(listPoints) < 5:
        newX = randomInt(-25,25)

        while newX in [point[0] for point in listPoints]:
            newX = randomInt(-25,25)

        newY = randomInt(-25,25)

        listPoints.append((newX, newY))
    Shape(listPoints[0][0],listPoints[0][1],listCoef[0],listPoints[1][0],listPoints[1][1],listCoef[1],listPoints[2][0],listPoints[2][1],listCoef[2],listPoints[3][0],listPoints[3][1],listCoef[3])
    
    print("coefs:", listCoef)
    print("points:", listPoints)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polynome d Hermite')
    plt.grid(True)

    ax = plt.gca()
    ax.set_aspect('equal', adjustable='datalim')

    # Definir un pas de 1 pour les graduations
    x_min, x_max = ax.get_xlim()  # Obtenir les limites de l'axe x
    y_min, y_max = ax.get_ylim()  # Obtenir les limites de l'axe y

    ax.set_xticks(np.arange(math.floor(x_min), math.ceil(x_max) + 1, 2))  # Pas de 1 en x
    ax.set_yticks(np.arange(math.floor(y_min), math.ceil(y_max) + 1, 2))  # Pas de 1 en y


DrawRandShape()

plt.show()