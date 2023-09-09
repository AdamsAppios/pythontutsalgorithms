class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Initialize the height of the node to 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        balance = self.get_balance(root)
        
        # Left-Left Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        
        # Right-Right Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        
        # Left-Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        # Right-Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
    
    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        
        return x
    
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

# Example usage:
avl_tree = AVLTree()
root = None
keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for key in keys:
    root = avl_tree.insert(root, key)

print("Inorder traversal of the AVL tree:")
avl_tree.inorder_traversal(root)
