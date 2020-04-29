class Node:

        def __init__(self, key):
            self.data = key
            self.left = None
            self.right = None


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)

def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data)
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)



def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:

            return lheight+1
        else:
            return rheight+1
























# Driver program to test above function
root = Node(4)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(5)
root.left.right = Node(3)

"Level order traversal of binary tree is -"
printLevelOrder(root)