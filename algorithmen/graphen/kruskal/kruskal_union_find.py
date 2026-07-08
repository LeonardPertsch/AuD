"""
Kruskal mit Union-Find
======================

Saubere Kruskal-Implementierung mit Union-Find-Struktur
(Pfadkompression + Union by Rank) zur Komponentenverwaltung.

Laufzeit: O(E log E)
"""

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

def kruskal(graph):
    edges = adj_list_to_edge_list(graph)
    sorted_edges = sort_edge_list_by_weight(edges)

    # Initialisierung der Zusammenhangskomponenten
    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}
    mst = []  # Liste für den minimalen Spannbaum

    def find(node):
        """Findet die Wurzel der Zusammenhangskomponente eines Knotens."""
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        """Vereint zwei Zusammenhangskomponenten."""
        root1 = find(node1)
        root2 = find(node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    # Kruskal-Algorithmus
    for node1, node2, weight in sorted_edges:
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append((node1, node2, weight))

    return mst

# Ausgabe des minimalen Spannbaums
mst = kruskal(graph)
print(mst)
