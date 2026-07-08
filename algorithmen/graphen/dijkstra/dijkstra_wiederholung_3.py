"""
Dijkstra (Klausur-Wiederholung 3, mit Ausgabe)
==============================================

Wiederholungsversion mit ausführlicher Konsolenausgabe: Start, Ziel,
Pfadkosten und Pfad.
"""

def dijkstra(graph, start, goal):

    w = {node: float('inf') for node in graph}
    w[start] = 0
    prev = {node:None for node in graph}

    unvisited = set(graph.keys())


    while unvisited:
        # Wähle den Knoten mit der aktuell kleinsten Distanz
        v_current = min(unvisited, key=lambda node: w[node])
        unvisited.remove(v_current)

        # Aktualisierung der Distanzen der Nachbarn
        for neighbor in graph[v_current]:
            new_distance = w[v_current] + graph[v_current][neighbor]  # Gewicht der Kante hinzufügen
            if new_distance < w[neighbor]:
                prev[neighbor] = v_current
                print(prev)
            w[neighbor] = min(w[neighbor], new_distance)  # Das Minimum wählen

    path = []
    current = goal
    while current is not None and current not in path:
        path.append(current)
        current = prev[current]

    path.reverse()





    print("StartKnoten:", start)
    print("GoalKnoten:", goal)
    print("Kosten für Path:", w[goal])
    print("Path:", path)
    return w


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3, 'E': 9},
    'D': {'B': 10, 'C': 3, 'E': 7, 'F': 8},
    'E': {'C': 9, 'D': 7, 'F': 4},
    'F': {'D': 8, 'E': 4}
}

dijkstra(graph, 'A', "F")
