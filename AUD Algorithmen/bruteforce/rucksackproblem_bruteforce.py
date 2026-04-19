from itertools import chain, combinations

# Liste der Items mit Name, Gewicht und Wert
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

def powerset(iterable):
    """Erzeugt alle möglichen Teilmengen einer Menge."""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def knapsack_bruteforce(G, w_max):
    v_max = 0
    A_max = []

    # Gehe alle Teilmengen von G durch
    for A in powerset(G):
        w_sum = sum(item["weight"] for item in A)  # Gesamtgewicht der Teilmenge
        v_sum = sum(item["value"] for item in A)  # Gesamtwert der Teilmenge

        # Falls gültig und bessere Lösung, aktualisieren
        if w_sum <= w_max and v_sum > v_max:
            A_max = A
            v_max = v_sum

    return v_max, A_max  # Beste Lösung zurückgeben

# Maximale Tragfähigkeit des Rucksacks
max_weight = 30

# **Algorithmus ausführen**
best_value, best_items = knapsack_bruteforce(items, max_weight)

# **Ergebnisse ausgeben**
print(f"Maximaler Wert im Rucksack: {best_value}")
print("Mitgenommene Items:")
for item in best_items:
    print(f"- {item['name']} (Wert: {item['value']}, Gewicht: {item['weight']})")
