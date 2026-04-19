graph = {
    0: [1, 2],
    1: [2, 3],
    2: [0, 3, 4],
    3: [4],
    4: [1]
}


def find_cycles(graph, start_node, goal_node):
    visited = set()
    cycles=[]
    dfs(start_node, graph, visited, [], cycles)
    for cycle in cycles:
        if start_node in cycle and goal_node in cycle:
            print("True")
            return True
    return cycles

def dfs(node, graph, visited, path, cycles):
    visited.add(node)
    path.append(node)
    for neighbour in graph.get(node,[]):
        print(path, visited)
        if neighbour in path:
            cycle_start = path.index(neighbour)
            cycles.append(path[cycle_start:])
        elif neighbour not in visited:
            dfs(neighbour, graph, visited, path, cycles)
    path.pop()

find_cycles(graph, 0, 2)