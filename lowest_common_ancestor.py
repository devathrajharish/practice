class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    # Stack for tree traversal
    stack = [root]

    # Dictionary for parent pointers
    parent = {root: None}

    # Iterate until we find both the nodes p and q
    while p not in parent or q not in parent:

        node = stack.pop()

        # While traversing the tree, keep saving the parent pointers.
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    # Ancestors set() for node p.
    ancestors = set()

    # Process all ancestors for node p using parent pointers.
    while p:
        ancestors.add(p)
        p = parent[p]

    # The first ancestor of q which appears in
    # p's ancestor set() is their lowest common ancestor.
    while q not in ancestors:
        q = parent[q]
    return q

root = Node(3)
root.left = Node(5)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right = Node(1)
root.right.left = Node(0)
root.right.right = Node(8)

print(lowestCommonAncestor(root, root.left, root.left.right.right).key)
