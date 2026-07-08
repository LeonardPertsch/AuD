"""
Einfache Zyklensuche
====================

Kompakte rekursive Zyklensuche: Landet die Suche auf einem bereits
besuchten Knoten, wird die besuchte Menge als Zyklus zurückgegeben.
"""

def find_cycles(graph):
    cycles = []
    for node in graph:
        visited = set()
        cycle = search_cycle(graph, node, visited)
        if cycle:
            cycles.append(cycle)
    return cycles

def search_cycle(graph, node, visited):
    if node in visited:
        return list(visited)  # Zyklus gefunden
    visited.add(node)
    for neighbor in graph.get(node):
        cycle = search_cycle(graph, neighbor, visited)
        if cycle:
            return cycle
    visited.remove(node)  # Rückgängig machen, falls kein Zyklus
    return None

# Test

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
print(find_cycles(graph2))
