class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

r = TreeNode(50)
for val in [30, 20, 40, 70, 60, 80]:
    insert(r, val)

print("In-order Traversal of BST:")
inorder(r)
print()
