class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Example usage:
root = None
keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]

for key in keys:
    root = insert(root, key)

print("Inorder traversal of the BST:")
inorder_traversal(root)
