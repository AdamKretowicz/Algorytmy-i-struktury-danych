graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
    }

from collections import defaultdict, deque

def bfs(graph, start):
    visited = set()  # Zbiór odwiedzonych wierzchołków
    queue = deque([start])  # Kolejka wierzchołków do odwiedzenia

    while queue:
        vertex = queue.popleft()  # Pobieranie wierzchołka z początku kolejki
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)  # Możesz zrobić coś z wierzchołkiem, np. wypisać go

            # Dodawanie sąsiadujących, nieodwiedzonych wierzchołków do kolejki
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

bfs(graph, 'A')#przykladowe dzialanie