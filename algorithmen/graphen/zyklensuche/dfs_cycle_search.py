"""
DFS-Zyklenerkennung (ungerichteter Graph)
=========================================

Erkennt per Tiefensuche alle Knoten, die auf einem Zyklus liegen, und
prüft, ob zwei Knoten im selben Zyklus liegen. Der Elternknoten wird
ignoriert, damit Kanten nicht fälschlich als Zyklus zählen.
"""

def dfs(adj_list, node, parent, path, visited, in_cycle):
    """ Tiefensuche zur Zykluserkennung """
    if node in path:  # Zyklus erkannt
        cycle_start = path.index(node)
        in_cycle.update(path[cycle_start:])  # Alle Knoten im Zyklus speichern
        return
    if node in visited:
        return

    visited[node] = 1  # Knoten als "im Stack" markieren
    path.append(node)

    for neighbor in adj_list.get(node):
        if neighbor != parent:  # Elternknoten ignorieren
            dfs(adj_list, neighbor, node, path, visited, in_cycle)

    path.pop()  # Knoten aus aktuellem Pfad entfernen
    visited[node] = 2  # Knoten als abgeschlossen markieren


def detect_cycles(adj_list):
    """ Gibt eine Menge von Knoten zurück, die in einem Zyklus sind """
    visited = {}  # Status jedes Knotens (nicht besucht, im Stack, abgeschlossen)
    in_cycle = set()  # Knoten, die in einem Zyklus liegen

    for node in adj_list:
        if node not in visited:
            dfs(adj_list, node, None, [], visited, in_cycle)

    return in_cycle


def are_nodes_in_same_cycle(adj_list, node1, node2):
    """ Prüft, ob beide Knoten in demselben Zyklus sind """
    cycle_nodes = detect_cycles(adj_list)
    print("Knoten in Zyklen:", cycle_nodes)
    return node1 in cycle_nodes and node2 in cycle_nodes


# Beispiel-Graph (ungerichtete Adjazenzliste)
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4, 6],
    6: [5]
}

# Test
node_a, node_b = 2, 3
print(are_nodes_in_same_cycle(graph, node_a, node_b))  # Sollte True sein
