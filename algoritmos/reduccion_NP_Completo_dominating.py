import matplotlib.pyplot as plt
import networkx as nx
from backtracking import bracktracking_hitting_set_problem


def reduce_dominating_set_to_hitting_set(grafo: nx.Graph):
    b_array = []

    for vertice in grafo.nodes:
        adyacentes = grafo.neighbors(vertice)
        set_adyacentes = set(adyacentes)
        set_adyacentes.add(vertice)
        b_array.append(set_adyacentes)

    return bracktracking_hitting_set_problem(b_array)


def prueba1():
    # Crear un grafo de ejemplo
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
    print(reduce_dominating_set_to_hitting_set(G))

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    plt.show()


def prueba2():
    G = nx.Graph()
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7),
        (4, 8), (5, 9), (5, 10), (6, 11), (7, 12), (8, 13),
        (9, 14), (10, 15), (11, 12), (12, 13), (13, 14), (14, 15)
    ]
    G.add_edges_from(edges)
    print(reduce_dominating_set_to_hitting_set(G))

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold',
            node_size=700, node_color='lightblue', font_size=8)
    plt.show()


def prueba3():
    G = nx.Graph()
    edges = [
        (1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (4, 7),
        (5, 7), (3, 6), (3, 7), (6, 7), (7, 12),
    ]
    G.add_edges_from(edges)
    print(reduce_dominating_set_to_hitting_set(G))

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold',
            node_size=700, node_color='lightblue', font_size=8)
    plt.show()


def prueba4():
    G = nx.Graph()
    edges = [
        (1, 6), (1, 4), (1, 3), (2, 5), (2, 4), (2, 7),
        (3, 5), (3, 8), (4, 9), (5, 10), (6, 7), (6, 10),
        (7, 8), (8, 9), (9, 10)
    ]
    G.add_edges_from(edges)
    print(reduce_dominating_set_to_hitting_set(G))

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold',
            node_size=700, node_color='lightblue', font_size=8)
    plt.show()
