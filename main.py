
# ==========================================
# BINARY TREE NODE
# ==========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ==========================================
# CREATE BINARY TREE
# ==========================================

def create_tree():
    root = Node("L")

    root.left = Node("A")
    root.right = Node("R")

    root.left.left = Node("I")
    root.left.right = Node("O")

    root.right.left = Node("S")
    root.right.right = Node("A")

    return root


# ==========================================
# OPTION 1: DISPLAY BINARY TREE
# ==========================================

def binary_tree():
    print("\nBINARY TREE - LARIOSA\n")

    print("              L")
    print("            /   \\")
    print("           A     R")
    print("          / \\   / \\")
    print("         I   O S   A")


# ==========================================
# OPTION 2: DISPLAY GRAPH
# ==========================================

graph = {
    "L": ["A", "R"],
    "A": ["L", "I", "O", "S"],
    "R": ["L", "S", "A2"],
    "I": ["A", "O"],
    "O": ["A", "I", "S"],
    "S": ["A", "R", "O"],
    "A2": ["R"]
}


def display_graph():
    print("\nGRAPH - LARIOSA\n")

    for vertex, connections in graph.items():
        print(vertex, "->", connections)


# ==========================================
# OPTION 3: BINARY TREE BFS AND DFS
# ==========================================

def bfs_tree(root):
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


def dfs_tree(root):
    if root is None:
        return []

    return [root.data] + dfs_tree(root.left) + dfs_tree(root.right)


def binary_tree_traversal():
    root = create_tree()

    print("\nBINARY TREE TRAVERSAL\n")

    print("BFS:", " -> ".join(bfs_tree(root)))
    print("DFS:", " -> ".join(dfs_tree(root)))


# ==========================================
# OPTION 4: GRAPH BFS AND DFS
# ==========================================

def bfs_graph(start):
    visited = {start}
    queue = [start]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def dfs_graph(current, visited=None):
    if visited is None:
        visited = set()

    visited.add(current)
    result = [current]

    for neighbor in graph[current]:
        if neighbor not in visited:
            result += dfs_graph(neighbor, visited)

    return result


def graph_traversal():
    print("\nGRAPH TRAVERSAL\n")

    print("BFS:", " -> ".join(bfs_graph("L")))
    print("DFS:", " -> ".join(dfs_graph("L")))


# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    while True:

        print("\n====================================")
        print("       LARIOSA NON-LINEAR DATA")
        print("              STRUCTURE")
        print("====================================")

        print("[1] Binary Tree")
        print("[2] Graph")
        print("[3] Binary Tree BFS and DFS")
        print("[4] Graph BFS and DFS")
        print("[5] Exit")

        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            binary_tree()

        elif choice == "2":
            display_graph()

        elif choice == "3":
            binary_tree_traversal()

        elif choice == "4":
            graph_traversal()

        elif choice == "5":
            print("\nThank you for using the program!")
            break

        else:
            print("\nInvalid choice! Please try again.")



if __name__ == "__main__":
    main()
