import numpy as np
import matplotlib.pyplot as plt
import math
from math import*

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
    
# Generer des valeurs x pour dessiner le polynome
        x_vals = np.linspace(ListPosX[i], ListPosX[i+1], 400)

# Calculer les valeurs y pour ces x en utilisant le polynome de Lagrange
        y_vals = [hermite(x, x_points, y_points, y_derived) for x in x_vals]

# Tracer le polynome de Lagrange et les points de donnees
        plt.plot(x_vals, y_vals, label=f'Segment {i + 1}', color='black')

# Courbe Exercice 2
def Trace():
        # C - E - F
        ListX = [-5,-2,1]
        ListY = [2,4,5]
        ListY_derived = [0, 6, -1]
        plotCurve(ListX, ListY, ListY_derived)
        
        # F - FF - G
        ListX = [1,4]
        ListY = [5,2]
        ListY_derived = [-10,-0.5]
        plotCurve(ListX, ListY, ListY_derived)

        # G -H
        ListX = [4,2]
        ListY = [2,-2]
        ListY_derived = [-8,-2]
        plotCurve(ListX, ListY, ListY_derived)

        # H - I
        ListX = [2,0]
        ListY = [-2,-1]
        ListY_derived = [5,-2]
        plotCurve(ListX, ListY, ListY_derived)

        # I - J
        ListX = [0,-4]
        ListY = [-1,-3]
        ListY_derived = [2,-6]
        plotCurve(ListX, ListY, ListY_derived)

        # J - K 
        ListX = [-4,-4.3]
        ListY = [-3,-2]
        ListY_derived = [0.2,3]
        plotCurve(ListX, ListY, ListY_derived)

        # K - L 
        ListX = [-4.3,-4]
        ListY = [-2,0]
        ListY_derived = [4,1]
        plotCurve(ListX, ListY, ListY_derived)

        # L - M 
        ListX = [-4,-2]
        ListY = [0,2]
        ListY_derived = [4,1]
        plotCurve(ListX, ListY, ListY_derived)

        # M - N  
        ListX = [-2,-1]
        ListY = [2,3]
        ListY_derived = [0.5,3]
        plotCurve(ListX, ListY, ListY_derived)

        # N  - O
        ListX = [-1,-1.2]
        ListY = [3,3.2]
        ListY_derived = [0.5,0.1]
        plotCurve(ListX, ListY, ListY_derived)

        # O - P - Q
        ListX = [-1.2,-3.3,-5]
        ListY = [3.2,2,1]
        ListY_derived = [1,-1,-1.5]
        plotCurve(ListX, ListY, ListY_derived)

        # Q - R 
        ListX = [-5,-6]
        ListY = [1,1]
        ListY_derived = [-1,1]
        plotCurve(ListX, ListY, ListY_derived)

        # R - S
        ListX = [-6,-6.2]
        ListY = [1,1.5]
        ListY_derived = [0.2,1.2]
        plotCurve(ListX, ListY, ListY_derived)

        # S - A 
        ListX = [-6.2,-6]
        ListY = [1.5,2]
        ListY_derived = [1.2,0.2]
        plotCurve(ListX, ListY, ListY_derived)
        
        # A - B - C
        ListX = [-6,-5.4,-5]
        ListY = [2,2.4,2]
        ListY_derived = [0.6,0.1,-1]
        plotCurve(ListX, ListY, ListY_derived)
        
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Polynome d Hermite')
        plt.grid(True)
        # plt.legend()

        ax = plt.gca()
        ax.set_aspect('equal', adjustable='datalim')

        # Definir un pas de 1 pour les graduations
        x_min, x_max = ax.get_xlim()  # Obtenir les limites de l'axe x
        y_min, y_max = ax.get_ylim()  # Obtenir les limites de l'axe y

        ax.set_xticks(np.arange(math.floor(x_min), math.ceil(x_max) + 1, 1))  # Pas de 1 en x
        ax.set_yticks(np.arange(math.floor(y_min), math.ceil(y_max) + 1, 1))  # Pas de 1 en y

Trace()


plt.show()
