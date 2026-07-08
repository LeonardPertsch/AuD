"""
Dijkstra mit Visualisierung
===========================

Dijkstra-Durchlauf, der jeden Relaxierungsschritt mit networkx und
matplotlib animiert darstellt.

Benötigt: networkx, matplotlib
"""

import networkx as nx
import matplotlib.pyplot as plt
import time


def dijkstra(graph, start):
    w = {node: float('inf') for node in graph}
    w[start] = 0
    unvisited = set(graph.keys())

    visited_edges = []  # Speichert Kanten für die Visualisierung

    while unvisited:
        v_current = min(unvisited, key=lambda node: w[node])
        unvisited.remove(v_current)

        for neighbor, weight in graph[v_current].items():
            new_distance = w[v_current] + weight
            if new_distance < w[neighbor]:
                w[neighbor] = new_distance
                visited_edges.append((v_current, neighbor, w[neighbor]))
                plot_graph(graph, visited_edges, pos)
                time.sleep(2)  # Verzögerung für die schrittweise Animation

    return w


def plot_graph(graph, visited_edges, pos):
    G = nx.Graph()

    # Kanten aus dem Graphen hinzufügen
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    plt.clf()

    # Zeichne alle Kanten
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    # Zeichne die besuchten Kanten farbig
    if visited_edges:
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v, _ in visited_edges], edge_color='red', width=2)

    plt.pause(0.1)  # Damit das Plotten aktualisiert wird


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3, 'E': 9},
    'D': {'B': 10, 'C': 3, 'E': 7, 'F': 8},
    'E': {'C': 9, 'D': 7, 'F': 4},
    'F': {'D': 8, 'E': 4}
}

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(nx.Graph(graph))  # Positionen werden einmalig berechnet
dijkstra(graph, 'A')
plt.show()
