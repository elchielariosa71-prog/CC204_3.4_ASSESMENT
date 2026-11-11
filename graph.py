# Create the graph using a dictionary
graph = {
    "L": ["A", "R"],
    "A": ["L", "I", "O", "S"],
    "R": ["L", "S", "A"],
    "I": ["A", "O"],
    "O": ["A", "I", "S"],
    "S": ["A", "R", "O"],
    "A2": ["R"]
}


# Display the Graph
print("GRAPH OF LARIOSA")
print()

for vertex in graph:
    print(vertex, "->", graph[vertex])