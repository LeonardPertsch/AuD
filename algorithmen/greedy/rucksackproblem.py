"""
Greedy: Rucksackproblem
=======================

Füllt den Rucksack, indem wiederholt das Item mit dem besten
Wert/Gewicht-Verhältnis gewählt wird. Liefert eine gute, aber nicht
zwingend optimale Lösung.

Laufzeit: O(n²) (Maximum-Suche in Schleife)
"""

import random
items = [
    {"name": "Infinity Edge", "weight": 8, "value": 3400},
    {"name": "Kraken Slayer", "weight": 7, "value": 3000},
    {"name": "Guardian Angel", "weight": 6, "value": 3200},
    {"name": "Rabadon's Deathcap", "weight": 9, "value": 3600},
    {"name": "Liandry's Anguish", "weight": 5, "value": 3200},
    {"name": "Luden's Tempest", "weight": 5, "value": 3200},
    {"name": "Trinity Force", "weight": 10, "value": 3333},
    {"name": "Goredrinker", "weight": 7, "value": 3200},

]
def knapsack_greedy(G, w_max):
    U = G
    A_max = [] #max Rucksackinhalt
    w_sum = 0 #Gewicht rucksackinhalt
    while w_sum != w_max and U != 0:
        if not U:
            break
        g_best = max(U, key=lambda g: g["value"] / g["weight"])
        U.remove(g_best)
        if w_sum + g_best["weight"] <= w_max:
            w_sum = w_sum + g_best["weight"]
            A_max.append(g_best)
    A_sum = 0
    for item in A_max:
        A_sum = A_sum + item["value"]
    return A_max, A_sum
knapsack = knapsack_greedy(items, 15)
print(knapsack)
