graph = {
    'A': [('B', 7), ('D', 5)],
    'B': [('A', 7), ('D', 9), ('E', 8), ('C', 7)],
    'C': [('B', 7), ('E', 5)],
    'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
    'E': [('B', 8), ('C', 5), ('D', 15), ('F', 8)],
    'F': [('D', 6), ('E', 8)]
}

def adj_list_to_edge_list(graph):
    edges = []
    seen_edges = set()  # Verhindert doppelte Kanten in ungerichteten Graphen

    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            edge = tuple(sorted([node, neighbor]))  # Sortiere, um (A, B) und (B, A) als gleich zu behandeln
            if edge not in seen_edges:
                edges.append((node, neighbor, weight))
                seen_edges.add(edge)  # Markiere die Kante als gesehen

    return edges

def sort_edge_list_by_weight(edge_list):
    """Sortiert die Kantenliste nach Kantengewicht aufsteigend."""
    return sorted(edge_list, key=lambda edge: edge[2])

edges = adj_list_to_edge_list(graph)
sorted_edges = sort_edge_list_by_weight(edges)

print(sorted_edges)
