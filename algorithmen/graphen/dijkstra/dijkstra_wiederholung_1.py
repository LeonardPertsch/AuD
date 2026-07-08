"""
Dijkstra (Klausur-Wiederholung 1)
=================================

Wiederholungsversion mit Vorgänger-Tracking und Pfad-Rekonstruktion
von Start zu Ziel.
"""

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3, 'E': 9},
    'D': {'B': 10, 'C': 3, 'E': 7, 'F': 8},
    'E': {'C': 9, 'D': 7, 'F': 4},
    'F': {'D': 8, 'E': 4}
}

def dijkstra(graph, start, goal):
    w = {node:float("inf") for node in graph}
    w[start] = 0
    unvisited = set(graph.keys())
    prev = {node:None for node in graph}

    while unvisited:
        v_current = min(unvisited, key=lambda node: w[node])
        unvisited.remove(v_current)
        for u in graph[v_current]:
            new_distance = w[v_current] + graph[v_current][u]
            if new_distance < w[u]:
                prev[u] = v_current

            w[u]= min(w[u], new_distance)
    path = []
    current = goal
    while current is not None and current not in path:
        path.append(current)
        current = prev[current]
    path.reverse()

    return path
print(dijkstra(graph, 'A', "B"))
