class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def maxpathsum(root):

    def helper(root):
        nonlocal max_sum
        if not root:
            return 0

        left_sum = max(helper(root.left),0)
        right_sum = max(helper(root.right), 0)
        path_sum = root.val + left_sum + right_sum
        max_sum = max(max_sum, path_sum)

        return root.val + max(left_sum, right_sum)


    max_sum = float('-inf')
    helper(root)
    return max_sum



root = Node(-10)
root.left = Node(9)
root.right = Node(20)

root.right.left = Node(15)
root.right.right = Node(7)
print(maxpathsum(root))