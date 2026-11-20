class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_tree():
    root = Node("L")

    root.left = Node("A")
    root.right = Node("R")

    root.left.left = Node("I")
    root.left.right = Node("O")

    root.right.left = Node("S")
    root.right.right = Node("A")

    return root

def binary_tree():

    print("\nBINARY TREE - LARIOSA\n")

    print("              L")
    print("            /   \\")
    print("           A     R")
    print("          / \\   / \\")
    print("         I   O S   A")

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

    return (
        [root.data]
        + dfs_tree(root.left)
        + dfs_tree(root.right)
    )


def binary_tree_traversal():

    root = create_tree()

    print("\nBINARY TREE TRAVERSAL\n")

    print(
        "BFS:",
        " -> ".join(bfs_tree(root))
    )

    print(
        "DFS:",
        " -> ".join(dfs_tree(root))
    )


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

            result += dfs_graph(
                neighbor,
                visited
            )

    return result


def graph_traversal():

    print("\nGRAPH TRAVERSAL\n")

    print(
        "BFS:",
        " -> ".join(
            bfs_graph("L")
        )
    )

    print(
        "DFS:",
        " -> ".join(
            dfs_graph("L")
        )
    )


def create_elchie_tree():

    root = Node("E")

    # LEFT SIDE
    root.left = Node("L")

    root.left.left = Node("H")
    root.left.right = Node("I")

    root.left.left.left = Node("A")
    root.left.left.right = Node("R")

    root.left.right.left = Node("I")
    root.left.right.right = Node("O")

    # RIGHT SIDE
    root.right = Node("C")

    root.right.left = Node("E")
    root.right.right = Node("L")

    root.right.left.left = Node("S")
    root.right.left.right = Node("A")

    return root


def preorder(root):

    if root is None:
        return []

    return (
        [root.data]
        + preorder(root.left)
        + preorder(root.right)
    )


def inorder(root):

    if root is None:
        return []

    return (
        inorder(root.left)
        + [root.data]
        + inorder(root.right)
    )


def postorder(root):

    if root is None:
        return []

    return (
        postorder(root.left)
        + postorder(root.right)
        + [root.data]
    )


def dfs_tree_methods():

    root = create_elchie_tree()

    print("\n====================================")
    print("         DFS METHODS IN TREE   ")
    print("        ELCHIE LARIOSA")
    print("====================================")

    print("\nTREE:\n")

    print("                  E")
    print("               /     \\")
    print("              L       C")
    print("            /   \\   /   \\")
    print("           H     I E     L")
    print("          / \\   / \\ / \\")
    print("         A   R I   O S   A")

    print("\nPreOrder")
    print("(Root -> Left -> Right):")
    print(" -> ".join(preorder(root)))

    print("\nInOrder")
    print("(Left -> Root -> Right):")
    print(" -> ".join(inorder(root)))

    print("\nPostOrder")
    print("(Left -> Right -> Root):")
    print(" -> ".join(postorder(root)))



# MAIN FUNCTION

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
        print("[5] DFS Methods in Tree")
        print("[6] Exit")

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

            dfs_tree_methods()

        elif choice == "6":

            print("\nThank you for using the program!")
            break

        else:

            print("\nInvalid choice! Please try again.")


# START PROGRAM

if __name__ == "__main__":
    main()