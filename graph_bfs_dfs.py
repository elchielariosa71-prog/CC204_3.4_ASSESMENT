# Create the Graph
graph = {
    "L": ["A", "R"],
    "A": ["L", "I", "O", "S"],
    "R": ["L", "S"],
    "I": ["A", "O"],
    "O": ["A", "I", "S"],
    "S": ["A", "R", "O"]
}


# -------------------------
# BFS - Breadth First Search
# -------------------------

def bfs(graph, start):

    visited = set()
    queue = [start]
    result = []

    visited.add(start)

    while queue:
        vertex = queue.pop(0)

        result.append(vertex)

        for neighbor in graph[vertex]:

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

    return result


# -------------------------
# DFS - Depth First Search
# -------------------------

def dfs(graph, vertex, visited=None):

    if visited is None:
        visited = set()

    visited.add(vertex)

    result = [vertex]

    for neighbor in graph[vertex]:

        if neighbor not in visited:

            result += dfs(graph, neighbor, visited)

    return result


# Display the results
print("GRAPH - LARIOSA")
print()

print("BFS:", " -> ".join(bfs(graph, "L")))

print("DFS:", " -> ".join(dfs(graph, "L")))