class Node:
    def __init__(self, data, color, parent=None):
        self.data = data
        self.color = color
        self.parent = parent
        self.left = None  # This should be set to NIL_LEAF later
        self.right = None  # This should be set to NIL_LEAF later

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None, 'black')
        self.root = self.NIL_LEAF

    def insert(self, data):
        new_node = Node(data, 'red', parent=self.NIL_LEAF)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF
        if self.root == self.NIL_LEAF:
            self.root = new_node
        else:
            self._insert_node(new_node, self.root)
        self._fix_insert(new_node)

    def _insert_node(self, new_node, current_node):
        if current_node != self.NIL_LEAF:
            if new_node.data < current_node.data:
                if current_node.left == self.NIL_LEAF:
                    current_node.left = new_node
                    new_node.parent = current_node
                else:
                    self._insert_node(new_node, current_node.left)
            elif new_node.data > current_node.data:
                if current_node.right == self.NIL_LEAF:
                    current_node.right = new_node
                    new_node.parent = current_node
                else:
                    self._insert_node(new_node, current_node.right)

    def rotate_left(self, node):
        right_child_tmp = node.right
        node.right = right_child_tmp.left
        if right_child_tmp.left != self.NIL_LEAF:
            right_child_tmp.left.parent = node
        right_child_tmp.parent = node.parent
        if node.parent is None:
            self.root = right_child_tmp
        elif node == node.parent.left:
            node.parent.left = right_child_tmp
        else:
            node.parent.right = right_child_tmp
        right_child_tmp.left = node
        node.parent = right_child_tmp

    def rotate_right(self, node):
        left_child_tmp = node.left
        node.left = left_child_tmp.right
        if left_child_tmp.right != self.NIL_LEAF:
            left_child_tmp.right.parent = node
        left_child_tmp.parent = node.parent
        if node.parent is None:
            self.root = left_child_tmp
        elif node == node.parent.right:
            node.parent.right = left_child_tmp
        else:
            node.parent.left = left_child_tmp
        left_child_tmp.right = node
        node.parent = left_child_tmp

    def _fix_insert(self, node):
        while node.parent.color == 'red':
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    uncle.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.rotate_left(node.parent.parent)
            else:
                uncle = node.parent.parent.right

                if uncle.color == 'red':
                    uncle.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent 
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.rotate_right(node.parent.parent)
        self.root.color = 'black'

def display_tree(node, indent="", position='root'):
    """Function to display the tree structure."""
    if node == tree.NIL_LEAF:
        return  # Exit if the node is a leaf

    # Get the node color
    color = node.color
    print(indent, node.data, f'({color})', f'- {position}')
    if node.left:
        display_tree(node.left, indent + "  ", 'L')
    if node.right:
        display_tree(node.right, indent + "  ", 'R')

# Testing
tree = RedBlackTree()
nums = [20, 15, 25, 10, 5, 1, 30, 35, 40]
for num in nums:
    tree.insert(num)

# Display the Red-Black Tree
print("Red-Black Tree after insertions:")
display_tree(tree.root)
