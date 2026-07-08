"""
Stochastisches Gradientenverfahren
==================================

Wie gradient_descent.py, aber statt des vollen Gradienten wird in jedem
Schritt eine zufällige Richtung y gewählt und entlang dieser abgestiegen.
"""

import numpy as np

def g(x):
    return sum(a ** 3 + a ** 2 for a in x)  # Summiert die Funktionswerte jeder Dimension

def stochastic_descent(x, n, delta_x, accuracy):
    x = list(x)  # Konvertiere x in eine Liste für Änderungen
    y = [0] * len(x)  # Initialisiere y als Nullvektor

    while g(x) > accuracy:
        for i in range(len(x)):
            y[i] = np.random.uniform(-1, 1)  # Zufälliger Richtungsvektor

        # Berechnung des Gradienten mit zentralem Differenzenquotienten
        x_plus = [xi + delta_x * yi for xi, yi in zip(x, y)]
        x_minus = [xi - delta_x * yi for xi, yi in zip(x, y)]
        delta_g = g(x_plus) - g(x_minus)

        # Norm von y für die Skalierung
        norm_y = sum(y_i**2 for y_i in y) + 1e-8  # Kleine Zahl zur Stabilität

        # Aktualisierung von x entlang der zufälligen Richtung y
        x = [xi - n * delta_g * yi / (2 * delta_x * norm_y) for xi, yi in zip(x, y)]

    return tuple(x)  # Konvertiere zurück in ein Tupel für die Ausgabe

# Aufruf des Algorithmus mit Beispielwerten
result = stochastic_descent((4, 1, 3), 0.01, 0.01, 1e-8)

# Ausgabe der Ergebnisse
print("Finaler Funktionswert:", g(result))
print("Gefundenes Minimum:", result)
