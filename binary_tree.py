class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the nodes
root = Node("L")

root.left = Node("A")
root.right = Node("R")

root.left.left = Node("I")
root.left.right = Node("O")

root.right.left = Node("S")
root.right.right = Node("A")


# Display the Binary Tree
print("BINARY TREE OF LARIOSA")
print()

print("              L")
print("            /   \\")
print("           A     R")
print("          / \\   / \\")
print("         I   O S   A")