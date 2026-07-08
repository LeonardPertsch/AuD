"""
Kruskal: minimaler Spannbaum
============================

Baut den minimalen Spannbaum auf: Kanten nach Gewicht sortieren
(eigener Mergesort) und aufnehmen, wenn sie zwei verschiedene
Zusammenhangskomponenten verbinden.

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
def sort_edge_list(edges):
    if len(edges) <= 1:
        return edges
    half = len(edges) // 2
    listL = sort_edge_list(edges[:half])
    listR = sort_edge_list(edges[half:])
    listS = []
    i,j = 0,0
    while i < len(listL) and j < len(listR):
        if listL[i][2] < listR[j][2]:
            listS.append(listL[i])
            i +=1
        else:
            listS.append(listR[j])
            j += 1
    listS.extend(listL[i:])
    listS.extend(listR[j:])
    return listS


def kruskal(graph):
    edges = sort_edge_list(adj_list_to_edge_list(graph))  # Schritt 1 & 2

    # Schritt 3: Initialisierung der Zusammenhangskomponenten
    f = {node: {node} for node in graph}  # Jede Zusammenhangskomponente enthält zunächst nur sich selbst
    print(f)
    # Schritt 4: Die Funktion gamma weist jedem Knoten seine aktuelle Zusammenhangskomponente zu
    gamma = {node: node for node in graph}  # Jeder Knoten gehört zu seiner eigenen Komponente
    print(gamma)
    # Schritt 5: Die Kantenliste des minimalen Spannbaums wird als leeres Tupel initialisiert
    mst = []

    # Schritt 6: Iteration über die sortierte Kantenliste
    for v1, v2, weight in edges:
        i = gamma[v1]  # Schritt 7: Index der Zusammenhangskomponente von v1
        j = gamma[v2]  # Schritt 8: Index der Zusammenhangskomponente von v2
        print(gamma)
        if i != j:  # Schritt 9: Falls die Knoten in verschiedenen Komponenten liegen
            # Schritt 10-13: Die kleinere Komponente wird mit der größeren verschmolzen
            if len(f[j]) > len(f[i]):
                temp = i
                i = j
                j = temp


            # Schritt 14-17: Alle Knoten von j werden zu i verschoben
            for u in f[j]:
                gamma[u] = i  # Schritt 15: gamma wird aktualisiert

            f[i].update(f[j])  # Schritt 16: Knoten von j in i schreiben
            f[j] = set()  # Schritt 17: Die j-te Komponente ist jetzt leer
            # Schritt 18: Kante zum MST hinzufügen
            mst.append((v1, v2, weight))

    # Schritt 19: Den minimalen Spannbaum zurückgeben
    return mst
print(kruskal(graph))
