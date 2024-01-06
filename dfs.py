graph = {
    "A": set(["B", "C"]),
    "B": set(["A", "D", "E"]),
    "C": set(["A", "F"]),
    "D": set(["B"]),
    "E": set(["B", "F"]),
    "F": set(["C", "E"]),
}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        # вершина
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# print(dfs(graph, 'A'))

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next_vertex in graph[start] - visited:
        dfs_recursive(graph, next_vertex, visited)
    return visited

# print(dfs_recursive(graph, 'A'))

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        vertex, path = stack.pop()
        for next_vertex in graph[vertex] - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            else:
                stack.append((next_vertex, path + [next_vertex]))

print(list(dfs_paths(graph, "A", "F")))