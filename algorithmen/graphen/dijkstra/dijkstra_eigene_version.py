"""
Dijkstra (eigene Übungsversion)
===============================

Selbst geschriebene Variante zum Üben – berechnet nur die Distanzen,
ohne Pfad-Rekonstruktion.
"""

def dijkstra(Graph, start):
    w= {node:float("inf") for node in Graph}
    unvisited = set(graph.keys())
    w[start]=0

    while unvisited:
        v_current = min(unvisited, key=lambda node: w[node])
        unvisited.remove(v_current)
        for neighbor in Graph[v_current]:
            new_distance =  w[v_current] + Graph[v_current][neighbor]
            w[neighbor] = min(new_distance,w[neighbor])

    return w

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3, 'E': 9},
    'D': {'B': 10, 'C': 3, 'E': 7, 'F': 8},
    'E': {'C': 9, 'D': 7, 'F': 4},
    'F': {'D': 8, 'E': 4}
}
print(dijkstra(graph,'A'))
