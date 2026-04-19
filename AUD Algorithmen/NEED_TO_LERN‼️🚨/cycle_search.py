graph = {
    0: [1, 2],
    1: [2, 3],
    2: [0, 3, 4],
    3: [4],
    4: [1]
}

def find_cycles(graph, start_node, goal_node):
    visited = set()  # Speichert bereits besuchte Knoten
    cycles = []  # Liste für gefundene Zyklen
    dfs(start_node, graph, visited, [], cycles)  # DFS starten
    for cycle in cycles:
        if start_node in cycle and goal_node in cycle:
            print("True")
            return True
    return cycles


def dfs(node, graph, visited, path, cycles):
    visited.add(node)  # Knoten als besucht markieren
    path.append(node)  # Knoten zum aktuellen Pfad hinzufügen

    for neighbor in graph.get(node, []):  # Alle Nachbarn durchgehen

        if neighbor in path:
            # Zyklus gefunden → Speichern
            cycle_start = path.index(neighbor)
            cycles.append(path[cycle_start:])
        elif neighbor not in visited:
            # Falls der Nachbar noch nicht besucht wurde, weiter mit DFS
            dfs(neighbor, graph, visited, path, cycles)

    path.pop()  # Knoten aus dem Pfad entfernen (Backtracking)
# Startknoten festlegen und Funktion aufrufen
start_node = 0
goal_node = 2
cycles_found = find_cycles(graph, start_node, goal_node)

# Ausgabe der gefundenen Zyklen
for cycle in cycles_found:
    print("Zyklus gefunden:", cycle)

