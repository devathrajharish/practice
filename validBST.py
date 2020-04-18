
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def validBST(root):
    if root == None:
        return 0

    stack = []
    inorder = [], float('-inf')

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if root.val <= inorder:
             return False

        inorder = root.val
        root = root.right

    return True



tree = TreeNode(2)
tree.left = TreeNode(1)
tree.rigt = TreeNode(3)

print(validBST(tree))