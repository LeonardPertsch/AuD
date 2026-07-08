"""
Zyklensuche Start/Ziel (auswendig geschrieben)
==============================================

Aus dem Gedächtnis geschriebene Version von cycle_search_start_ziel.py
als Klausurvorbereitung.
"""

graph = {
    0: [1, 2],
    1: [2, 3],
    2: [0, 3, 4],
    3: [4],
    4: [1]
}


def cycle_search(graph, start, end):
    cycles = []
    visited = set()
    dfs(graph, start, visited, [], cycles)
    for cycle in cycles:
        if start in cycle and end in cycle:
            print("True")
            return True
    print(False)
    return False



def dfs(graph, node, visited, path, cycles):
    visited.add(node)
    path.append(node)
    for neighbour in graph.get(node, []):
        if neighbour in path:
            cycle_start = path.index(neighbour)
            cycles.append(path[cycle_start:])
        elif neighbour not in visited:
            dfs(graph, neighbour,visited, path, cycles)

    path.pop()

cycle_search(graph,0,2)
