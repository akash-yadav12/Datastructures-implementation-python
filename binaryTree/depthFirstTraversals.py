class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.data,"--->",end="")
    inorder(root.right)
def postorder(root):
    if not root:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.data,'--->',end="")
def preorder(root):
    if not root:
        return None
    print(root.data,'--->',end="")
    preorder(root.left)
    preorder(root.right)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(6)
    root.left.left = Node(4)
    root.left.right = Node(2)
    print('inorder Traversal:')
    inorder(root)
    print()
    print('post order traversal:')
    postorder(root)
    print()
    print('preoder traversal')
    preorder(root)