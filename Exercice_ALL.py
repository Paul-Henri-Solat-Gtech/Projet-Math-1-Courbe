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

def factorial(n):
    fact = 1
    for i in range(n):
        fact *= n - i
    return(fact)

def cos(x):
    signe = -1
    fcos = 0
    for n in range(100):
        if n % 2 != 0:  # Si n n'est pas un multiple de 2
            continue
        signe *= -1

        fcos += (signe * ((x**n)/factorial(n)))

    return fcos

def sin(x):
    return cos(pi/2 - x)

def drawEllipse(posX, posY, sizeX, sizeY):
    
    teta = np.linspace(0, 2*pi, 400)  # 400 points entre 0 et 2pi
    
    # Calculer les valeurs de x
    x_values = sizeX*cos(teta) + posX
    # Calculer les valeurs de f(x)
    y_values = sizeY*sin(teta) + posY

    # Tracer la courbe
    plt.plot(x_values, y_values, label="f(x) = cos(x)", color="blue")

    # Ajouter des etiquettes et un titre
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Courbe de f(x) = cos(x)")

    # Afficher le graphique
    plt.grid(True)
    plt.show()

def lagrange(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

def DrawLagrangeExample():
    
    # Exemple de points 
    x_points = [-6.3,-6,-5.5,-5,-2,1,4]
    y_points = [1.5,2,2.3,2,4,5,2]

    lastXindex = len(x_points) -1

    plt.title('Polynome de Lagrange')
    plt.grid(True)
    plt.legend()

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

def Mirror(ListPosX, ListPosY, ListPosY_derived):
    newListX = ListPosX[::-1]
    newListY = [-x for x in ListPosY[::-1]]
    newListY_derived =ListPosY_derived[::-1]
    n=len(newListX)
    for i in range(n-1):
        x_points = [newListX[i],newListX[i+1]]
        y_points = [newListY[i],newListY[i+1]]
        y_derived = [newListY_derived[i],newListY_derived[i+1]]
    
    # Generer des valeurs x pour dessiner le polynome
        x_vals = np.linspace(newListX[i], newListX[i+1], 400)

    # Calculer les valeurs y pour ces x en utilisant le polynome de Lagrange
        y_vals = [hermite(x, x_points, y_points, y_derived) for x in x_vals]

    # Tracer le polynome de Lagrange et les points de donnees
        plt.plot(x_vals, y_vals, label=f'Segment {i + 1}', color='red')

def Trace():
        # C - D - E - F
        ListX = [-5,-2,1]
        ListY = [2,4,5]
        ListY_derived = [0, 6, -1]
        plotCurve(ListX, ListY, ListY_derived)
        Mirror(ListX, ListY, ListY_derived)
        
        # F - FF - G
        ListX = [1,4]
        ListY = [5,2]
        ListY_derived = [-10,-0.5]
        plotCurve(ListX, ListY, ListY_derived)
        Mirror(ListX, ListY, ListY_derived)
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

def Shape(xA,yA,yyA,xB,yB,yyB,xC,yC,yyC,xD,yD,yyD):    
        
        # A - B - C - D
        ListX = [xA, xB, xC, xD, xA]
        ListY = [yA, yB, yC, yD, yA]
        ListY_derived = [yyA, yyB, yyC, yyD,yyA]
        plotCurve(ListX, ListY, ListY_derived)
        # Mirror(ListX, ListY, ListY_derived)



def DrawRandShape():
    listPoints = []
    listCoef = []

    while len(listCoef) < 5 :
        newCoef = randomFloat(-5,5)
        listCoef.append(newCoef)

    while len(listPoints) < 5:
        newX = randomInt(-25,25)

        if len(listPoints) > 0:
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



# Courbe exo 2
def TraceEXO2():
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

        ax = plt.gca()
        ax.set_aspect('equal', adjustable='datalim')

        x_min, x_max = ax.get_xlim()  
        y_min, y_max = ax.get_ylim()  

        # Definir un pas de 1 pour les graduations
        ax.set_xticks(np.arange(math.floor(x_min), math.ceil(x_max) + 1, 1)) 
        ax.set_yticks(np.arange(math.floor(y_min), math.ceil(y_max) + 1, 1)) 

# Fonction demandée pour exo 1
# drawEllipse(0,0,15,1)

# Fonction demandée pour exo 2
# TraceEXO2()

# Exo 3
DrawRandShape()

plt.show()