class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def Levels(root):

    levels = []
    if not root:
        return levels

    def helper(root, level):

        if len(levels) == level:
            levels.append([])

        levels[level].append(root.val)

        if root.left:
            helper(root.left, level + 1)
        if root.right:
            helper(root.right, level + 1)

    helper(root, 0)
    return levels



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(Levels(root))