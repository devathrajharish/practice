class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def search(root,key):

    if root is None or root.val == key:
        return root

    if (root.val<key):
        return search(root.right, key)
    else:
        return search(root.left,key)

def insert(root, key):
    if root is None:
        root = key

    else:
        if root.val < key.val:
            if root.right is None:
                root.right = key
            else:
                insert(root.right, key)

        else:
            if root.left is None:
                root.left = key
            else:
                insert(root.left, key)


def minValueNOde(node):
    current = Node
    while(current.left is not  None):
        current = current.left

    return current


def delete(root, key):
    if root is None:
        return root

    if key > root.val:
        root.right = delete(root.right, key)

    elif key < root.val:
        root.left = delete(root.left, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        else:
            temp = root.left
            root = None
            return  temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)


    return root





def inorder(root):
    if root:

        inorder(root.left)
        print(root.val)
        inorder(root.right)








r = Node(50)
insert(r, Node(30))
insert(r,Node(34))
insert(r,Node(70))
insert(r,Node(80))
inorder(r)

delete(r,34)
print("\n")
inorder(r)
delete(r,30)
print("\n")
inorder(r)