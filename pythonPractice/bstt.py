class Node:                 #class for creating node

    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data


def insert(root,node):
    if root is None:
        root=Node
    else:
        if root.data<node.data:             #if data to be inserted is greater than root, insert it in the right side of root
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)  #make recursive call until data is inserted
        else:
            if root.data>node.data:         #if data to be inserted is less than root, insert it in the left side of root
                if root.left is None:
                    root.left=node
                else:
                    insert(root.left,node)

def inorder(root):   #traversal method
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


root = Node(2)
insert(root,Node(8))
insert(root,Node(7))
insert(root,Node(6))
insert(root,Node(4))
insert(root,Node(10))
insert(root,Node(3))
inorder(root)

