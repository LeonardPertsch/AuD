def dijkstra(graph, start):

    w = {node: float('inf') for node in graph}
    w[start] = 0
    previous = {node: None for node in graph}
    unvisited = set(graph.keys())

    while unvisited:
        v_current = min(unvisited, key=lambda node: w[node])
        unvisited.remove(v_current)

        for neighbor in graph[v_current]:
            new_distance = w[v_current] + graph[v_current][neighbor]
            if new_distance < w[neighbor]:
                w[neighbor] = new_distance
                previous[neighbor] = v_current

    return w, previous


def shortest_path(graph, start, goal):
    distances, previous = dijkstra(graph, start)
    path = []
    node = goal
    while node is not None:
        path.insert(0, node)
        node = previous[node]
    print(f"Kürzester Weg von {start} nach {goal}: {path}")
    print(f"Gesamtkosten: {distances[goal]}")
    return path, distances[goal]


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3, 'E': 9},
    'D': {'B': 10, 'C': 3, 'E': 7, 'F': 8},
    'E': {'C': 9, 'D': 7, 'F': 4},
    'F': {'D': 8, 'E': 4}
}

shortest_path(graph, 'A', 'F')
