graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Zbiór odwiedzonych wierzchołków
    
    visited.add(start)
    print(start)  # Możesz zrobić coś z wierzchołkiem, np. wypisać go

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

dfs(graph, 'A')#przykładowe działanie