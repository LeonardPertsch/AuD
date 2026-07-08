"""
Einfache Zyklensuche (eigene Übungsversion)
===========================================

Selbst geschriebene Variante von easy_cycle_search.py zum Üben.
"""

def main(Graph):
    circles = []
    for node in Graph:
        visited = set()
        circle = search(Graph, node,visited)
        circles.append(circle)
    return circles

def search(Graph, node, visited):
    if node in visited:
        return list(visited)
    visited.add(node)
    for neighbour in Graph[node]:
        cycle = search(Graph, neighbour, visited)
        if cycle:
            return cycle
    return None



graph2 = {
    1: {7},
    2: {16},
    4: {89},
    5: {95},
    6: {29},
    7: {1},
    10: {32, 43, 54},
    11: {99},
    13: {97},
    16: {2},
    21: {32, 43, 54},
    23: {72},
    24: {60},
    29: {6},
    32: {10, 21},
    43: {10, 21},
    54: {10, 21},
    53: {78},
    56: {98},
    60: {24},
    64: {97},
    65: {68},
    68: {65},
    72: {23},
    78: {53},
    89: {4},
    95: {5},
    97: {13, 64},
    98: {56},
    99: {11}
}
print(main(graph2))
