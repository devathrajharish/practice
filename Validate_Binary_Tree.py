class newNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if not root:
        return

    print(root.val)
    preorder(root.left)
    preorder(root.right)

def validate_tree(root):
    def helper(node, lower=float('-inf'), upper=float('inf')):

        if not node:
            return True

        val = node.val

        if val <= lower or val >= upper:
            return False

        return helper(node.right, val, upper) and helper(node.left, lower, val)
    return helper(root)







if __name__ == '__main__':
    root = newNode(2)
    root.left = newNode(1)
    # root.left.left = newNode(8)
    # root.right = newNode(12)
    # root.right.left = newNode(11)
    # root.right.right = newNode(22)
    root.right = newNode(3)

    print("Inorder traversal before insertion:", end=" ")
    preorder(root)

    print(validate_tree(root))

    print()
    print("Inorder traversal after insertion:", end=" ")
    preorder(root)