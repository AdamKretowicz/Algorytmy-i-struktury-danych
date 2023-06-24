"""import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def build_graph():
    print("Podaj typ grafu:")
    print("1. Skierowany")
    print("2. Nieskierowany")

    while True:
        try:
            graph_type = int(input("Wybierz opcję (1 lub 2): "))
            if graph_type in [1, 2]:
                break
            else:
                print("Niepoprawny wybór. Wybierz 1 lub 2.")
        except ValueError:
            print("Niepoprawny wybór. Wybierz 1 lub 2.")

    num_vertices = int(input("Podaj liczbę wierzchołków: "))

    adjacency_matrix = np.zeros((num_vertices, num_vertices))
    adjacency_list = [[] for _ in range(num_vertices)]

    num_edges = int(input("Podaj liczbę połączeń: "))
    print("Dla każdego połączenia, podaj numery wierzchołków, które są połączone.")

    for _ in range(num_edges):
        while True:
            try:
                vertex1 = int(input("Pierwszy wierzchołek: "))
                vertex2 = int(input("Drugi wierzchołek: "))

                if vertex1 < 0 or vertex1 >= num_vertices or vertex2 < 0 or vertex2 >= num_vertices:
                    print("Niepoprawny numer wierzchołka. Spróbuj ponownie.")
                else:
                    break
            except ValueError:
                print("Niepoprawny numer wierzchołka. Spróbuj ponownie.")

        weight = float(input("Podaj wagę połączenia (jeśli graf jest nieważony, wpisz 1): "))

        adjacency_matrix[vertex1][vertex2] = weight
        adjacency_list[vertex1].append((vertex2, weight))

        if graph_type == 2:  # Nieskierowany graf
            adjacency_matrix[vertex2][vertex1] = weight
            adjacency_list[vertex2].append((vertex1, weight))

    print("\nMacierz sąsiedztwa:")
    print(adjacency_matrix)

    print("\nLista sąsiedztwa:")
    for i in range(num_vertices):
        print(f"{i}: {adjacency_list[i]}")

    # Tworzenie grafu za pomocą biblioteki networkx
    G = nx.DiGraph() if graph_type == 1 else nx.Graph()

    for i in range(num_vertices):
        G.add_node(i)

    for i in range(num_vertices):
        for j in range(num_vertices):
            if adjacency_matrix[i][j] != 0:
                G.add_edge(i, j, weight=adjacency_matrix[i][j])

    # Rysowanie grafu
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

    # Algorytm Dijkstry
    start_vertex = int(input("Podaj wierzchołek początkowy dla algorytmu Dijkstry: "))

    # Inicjalizacja
    distances = {v: float('inf') for v in range(num_vertices)}
    distances[start_vertex] = 0
    visited = set()

    while len(visited) < num_vertices:
        # Wybierz wierzchołek o najmniejszej odległości
        current_vertex = min(set(distances.keys()) - visited, key=distances.get)

        # Zaznacz bieżący wierzchołek jako odwiedzony
        visited.add(current_vertex)

        # Aktualizuj odległości do sąsiadów bieżącego wierzchołka
        for neighbor, weight in adjacency_list[current_vertex]:
            new_distance = distances[current_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    # Wyświetl najkrótsze odległości
    print("\nNajkrótsze odległości od wierzchołka początkowego:")
    for v in range(num_vertices):
        print(f"{v}: {distances[v]}")


build_graph()"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def build_graph():
    print("Podaj typ grafu:")
    print("1. Skierowany")
    print("2. Nieskierowany")

    while True:
        try:
            graph_type = int(input("Wybierz opcję (1 lub 2): "))
            if graph_type in [1, 2]:
                break
            else:
                print("Niepoprawny wybór. Wybierz 1 lub 2.")
        except ValueError:
            print("Niepoprawny wybór. Wybierz 1 lub 2.")

    num_vertices = int(input("Podaj liczbę wierzchołków: "))

    adjacency_matrix = np.zeros((num_vertices, num_vertices))
    adjacency_list = [[] for _ in range(num_vertices)]

    num_edges = int(input("Podaj liczbę połączeń: "))
    print("Dla każdego połączenia, podaj numery wierzchołków, które są połączone.")

    for _ in range(num_edges):
        while True:
            try:
                vertex1 = int(input("Pierwszy wierzchołek: "))
                vertex2 = int(input("Drugi wierzchołek: "))

                if vertex1 < 0 or vertex1 >= num_vertices or vertex2 < 0 or vertex2 >= num_vertices:
                    print("Niepoprawny numer wierzchołka. Spróbuj ponownie.")
                else:
                    break
            except ValueError:
                print("Niepoprawny numer wierzchołka. Spróbuj ponownie.")

        weight = float(input("Podaj wagę połączenia: "))

        adjacency_matrix[vertex1][vertex2] = weight
        adjacency_list[vertex1].append((vertex2, weight))

        if graph_type == 2:  # Nieskierowany graf
            adjacency_matrix[vertex2][vertex1] = weight
            adjacency_list[vertex2].append((vertex1, weight))

    print("\nMacierz sąsiedztwa:")
    print(adjacency_matrix)

    print("\nLista sąsiedztwa:")
    for i in range(num_vertices):
        print(f"{i}: {adjacency_list[i]}")

    # Tworzenie grafu za pomocą biblioteki networkx
    G = nx.DiGraph() if graph_type == 1 else nx.Graph()

    for i in range(num_vertices):
        G.add_node(i)

    for i in range(num_vertices):
        for j in range(num_vertices):
            if adjacency_matrix[i][j] != 0:
                if graph_type == 2 and i < j and adjacency_matrix[j][i] != 0:
                    # Dodaj dwa połączenia między tymi samymi wierzchołkami
                    G.add_edge(i, j, weight=adjacency_matrix[i][j])
                    G.add_edge(j, i, weight=adjacency_matrix[j][i])
                else:
                    # Dodaj pojedyncze połączenie
                    G.add_edge(i, j, weight=adjacency_matrix[i][j])

    # Rysowanie grafu
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

    # Algorytm Dijkstry
    start_vertex = int(input("Podaj wierzchołek początkowy dla algorytmu Dijkstry: "))

    # Inicjalizacja
    distances = {v: float('inf') for v in range(num_vertices)}
    distances[start_vertex] = 0
    visited = set()

    while len(visited) < num_vertices:
        # Wybierz wierzchołek o najmniejszej odległości
        current_vertex = min(set(distances.keys()) - visited, key=distances.get)

        # Zaznacz bieżący wierzchołek jako odwiedzony
        visited.add(current_vertex)

        # Aktualizuj odległości do sąsiadów bieżącego wierzchołka
        for neighbor, weight in adjacency_list[current_vertex]:
            new_distance = distances[current_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    # Wyświetl najkrótsze odległości
    print("\nNajkrótsze odległości od wierzchołka początkowego:")
    for v in range(num_vertices):
        print(f"{v}: {distances[v]}")


build_graph()
