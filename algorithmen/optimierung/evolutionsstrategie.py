"""
Evolutionsstrategie: Wurzelberechnung
=====================================

Nähert eine Wurzel über einen evolutionären Algorithmus an:
Rekombination, Mutation (normalverteiltes Rauschen) und Selektion des
besten Individuums über viele Generationen.

Benötigt: numpy
"""

import random
import numpy

def sqrt(number):
    # Initialisiere die Elternliste mit zufälligen Werten
    parents = [random.uniform(0, 1000) for _ in range(1000)]

    children = []
    for i in range(1, 100):
        children = recombine(parents)  # Rekombiniere die Eltern
        children = mutate(number, children)  # Mutieren der Kinder
        parents = parents + children  # Füge die Kinder zu den Eltern hinzu
        parents = select(number, parents)  # Wähle das beste Elternteil
    return parents[0]  # Rückgabe des besten Werts

def recombine(parents):
    # Hier wird das erste Elternteil vervielfältigt (dies ist eine einfache Rekombination)
    return [parents[0], parents[0]]

def g(number, x):
    # Berechne den Fehler, wie nahe x^2 an der Zahl number ist
    return abs(number - x * x * x)

def mutate(number, list):
    s = []
    for i in range(len(list)):
        r = numpy.random.normal(0, 1)  # Generiere eine Zufallszahl aus der Normalverteilung
        z = g(number, list[i])  # Berechne den Fehler
        s.append(list[i] * (1 + 0.1 * z * r))  # Mutieren des Werts
    return s  # Rückgabe der mutierten Liste

def select(number, list):
    # Wähle das Elternteil mit dem geringsten Fehler aus
    g_min = g(number, list[0])
    k = 0
    for i in range(1, len(list)):
        if g_min > g(number, list[i]):
            g_min = g(number, list[i])
            k = i
    return [list[k]]  # Rückgabe des besten Elternteils in einer Liste

# Beispielaufruf der Funktion sqrt(4)
print(sqrt(160))
