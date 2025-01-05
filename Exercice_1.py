import numpy as np
import matplotlib.pyplot as plt
from math import py

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

    # Afficher la legende
    # plt.legend()

    # Afficher le graphique
    plt.grid(True)
    plt.show()

drawEllipse(0,0,15,1)
    
plt.show()
