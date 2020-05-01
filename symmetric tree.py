class Node:

    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def isSymmetric(root):
    if (root is None): return True
    queue = [(root.left, root.right)]
    while (queue):

        node1, node2 = queue.pop(0)
        if (node1 is None and node2 is None): continue
        if (None in [node1, node2]): return False
        if (node1.val != node2.val): return False
        queue.append((node1.left, node2.right))
        queue.append((node1.right, node2.left))
    return True

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.right = Node(3)
root.right.left = Node(4)

print(isSymmetric(root))