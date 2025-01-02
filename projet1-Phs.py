import matplotlib.pyplot as plt
import numpy as np
import math

def factoriel(n):
    s = 1
    for i in range(n):
        s *= n - i
    return(s)

def cosinus(x) :
    s=0
    for i in range(20):
        #s = somme
        s+= (x**(2*i)*(-1)**i) / factoriel(2*i)
    return(s)

def sinus(x):
    sin = cosinus((math.pi / 2) - x)
    return(sin)

def ellipse(xC, yC, a, b):
    nbPoints = 50

    C = [xC, yC]
    X = []
    Y = []

    # Taylor
    for i in range(nbPoints + 1):
        theta = 2 * math.pi * i / nbPoints
        x = a * cosinus(theta)
        y = b * sinus(theta)
        X.append(xC + x)
        Y.append(yC + y)
    
    plt.scatter([xC], [yC], color="red", label="Centre (xC, yC)") 
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(X,Y)
    plt.grid(True)

def trace():
    x = [0, 2, 4, 1, -5, -5, -1, -4, 0]
    y = [-1, -2, 2, 5, 3, 1, 2, -3, -1]

    plt.scatter(x, y, color='red', label='Points')
    plt.plot(x, y, color='blue', label='Ligne')
    plt.grid(True)
    return

def ex3Lagrange():
    L = [[0,2,3],[-1,-2,2]]

    x_values = np.linspace(0, 2, 40)  # Générer des points x entre -2 et 2
    y_values = []  # Liste pour stocker les valeurs de y correspondantes
    
    for x in x_values:
        l1 = ((x - L[0][1]) * (x - L[0][2])) / ((L[0][0]-L[0][1]) * (L[0][0]-L[0][2]))
        l2 = ((x - L[0][0]) * (x - L[0][2])) / ((L[0][1]-L[0][0]) * (L[0][1]-L[0][2]))
        l3 = ((x - L[0][0]) * (x - L[0][1])) / ((L[0][2]-L[0][0]) * (L[0][2]-L[0][1]))
        
        Plx = l1*L[1][0] + l2*L[1][1] + l3*L[1][2]
        y_values.append(Plx)
    
    plist = []
    l = len(L[0])
    for i in range(l):
        p = 1
        for j in range(l):
            if i != j:
                p *= (x - L[0][j]) / (L[0][i] - L[0][j])
                plist.append(p)
    plx = sum(plist[i] * L[1][i] for i in range(l))
    
    # Tracer la courbe d'interpolation
    plt.plot(x_values, y_values, label="Interpolation de Lagrange", color='b')

    # Ajouter les points donnés
    plt.scatter(L[0], L[1], color='red', zorder=5, label="Points donnés")
    plt.grid(True)

#ellipse(0,5,30,10)
trace()
ex3Lagrange()
plt.show()