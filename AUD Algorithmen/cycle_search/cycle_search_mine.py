
def cylces_search_main(G):
    cycless=[]
    for node in G:
        visited = {node:[False, []] for node in G}

        dacycle = cycle_search(G, node, visited)
        cycless.append(dacycle)
    return cycless

def cycle_search(graph, node, visited):

    visited[node][0]=True
    for neighbor in graph[node]:
        if not visited[neighbor][0]:
            cycle=cycle_search(graph, neighbor, visited)
            if cycle:
                return cycle
        else:
            cycle = [visited_node for visited_node in visited if visited[visited_node][0]]
    return cycle


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
print(cylces_search_main(graph2))