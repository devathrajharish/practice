class Node:

    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = None


def minValue(node):
    current = node

    # loop down to find the lefmost leaf
    while (current.left is not None):
        current = current.left

    return current.data



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(minValue(root))