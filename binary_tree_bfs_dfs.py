class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the Binary Tree
root = Node("L")

root.left = Node("A")
root.right = Node("R")

root.left.left = Node("I")
root.left.right = Node("O")

root.right.left = Node("S")
root.right.right = Node("A")


# -------------------------
# BFS - Breadth First Search
# -------------------------

def bfs(root):
    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)

        result.append(current.data)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result


# -------------------------
# DFS - Depth First Search
# -------------------------

def dfs(root):
    if root is None:
        return []

    result = [root.data]

    result += dfs(root.left)
    result += dfs(root.right)

    return result


# Display the result
print("BINARY TREE - LARIOSA")
print()

print("BFS:", " -> ".join(bfs(root)))

print("DFS:", " -> ".join(dfs(root)))