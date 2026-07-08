"""
DFS-Zyklensuche mit Visualisierung
==================================

Animierte Tiefensuche: besuchte Knoten, betrachtete Kanten und gefundene
Zyklen werden schrittweise mit networkx/matplotlib eingefärbt.

Benötigt: networkx, matplotlib
"""

import networkx as nx
import matplotlib.pyplot as plt
import time

# Beispiel-Graph als Adjazenzliste
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4, 6],
    6: [5]
}

# Erstelle Graph mit NetworkX
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Position der Knoten für eine einheitliche Darstellung
pos = nx.spring_layout(G, seed=42)


# Visualisierungsfunktion
def plot_graph(highlight_nodes=None, highlight_edges=None, cycle_nodes=None):
    plt.figure(figsize=(6, 6))

    # Zeichne alle Knoten und Kanten in Standardfarbe
    nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="gray", node_size=700, font_size=15)

    # Markiere aktuell besuchte Knoten (orange)
    if highlight_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes, node_color="orange", node_size=700)

    # Markiere aktuell betrachtete Kanten (rot)
    if highlight_edges:
        nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color="red", width=2)

    # Markiere Knoten im Zyklus (blau)
    if cycle_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=cycle_nodes, node_color="blue", node_size=700)

    # Print aktuellen Stand von path und visited
    print(f"Path: {path}")
    print(f"Visited: {visited}")
    print("-" * 30)

    plt.show(block=False)  # Zeige das Bild an
    plt.pause(3)  # Warte 3 Sekunden
    plt.close()  # Schließe das Bild, um das nächste sauber zu zeichnen


# Tiefensuche mit Visualisierung
visited = set()
path = []


def dfs(node, parent):
    if node in path:
        # Zyklus erkannt
        cycle_start = path.index(node)
        cycle_nodes = path[cycle_start:]
        print(f"Zyklus gefunden: {cycle_nodes}")
        plot_graph(highlight_nodes=[node], cycle_nodes=cycle_nodes)
        return

    if node in visited:
        return

    visited.add(node)
    path.append(node)

    # Visualisiere aktuellen Knoten
    plot_graph(highlight_nodes=[node])

    for neighbor in graph[node]:
        if neighbor == parent:  # Ignoriere den Parent-Knoten
            continue

        # Visualisiere die aktuelle Kante, die betrachtet wird
        plot_graph(highlight_nodes=[node, neighbor], highlight_edges=[(node, neighbor)])

        dfs(neighbor, node)

    path.pop()  # Knoten aus dem Pfad entfernen


# Starte Visualisierung mit DFS von Knoten 1
dfs(1, None)
