class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):

    if data <= root.data:
   
        if root.left is None:
            root.left = Node(data)
        else:
            insert(root.left, data)
    else:
        if root.right is None:
            root.right = Node(data)
        else:
            insert(root.right,data)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

if __name__ == "__main__":
    r = Node(40)
    insert(r,20)
    insert(r,50)
    insert(r,17)
    inorder(r)
    

    

    