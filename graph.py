def create_adjacency_list(graph):
    adjacency_list = {}
    for node in graph:
        adjacency_list[node] = []
        for neighbor in graph[node]:
            adjacency_list[node].append(neighbor)
    return adjacency_list

# example case
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

adjacency_list = create_adjacency_list(graph)
print(adjacency_list)