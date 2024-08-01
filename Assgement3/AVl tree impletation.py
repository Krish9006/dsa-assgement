class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        
        self.update_height(node)
        balance = self.get_balance(node)
        
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_larger_node = self.find_min(node.right)
            node.key = min_larger_node.key
            node.right = self.delete(node.right, min_larger_node.key)
        
        self.update_height(node)
        balance = self.get_balance(node)
        
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node

    def find(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.find(node.left, key)
        else:
            return self.find(node.right, key)

    def get_size(self, node):
        if not node:
            return 0
        return self.get_size(node.left) + 1 + self.get_size(node.right)

    def order_of_key(self, node, key):
        if not node:
            return 0
        if key <= node.key:
            return self.order_of_key(node.left, key)
        else:
            return self.get_size(node.left) + 1 + self.order_of_key(node.right, key)

    def get_by_order(self, node, k):
        if not node:
            return None
        left_size = self.get_size(node.left)
        if k < left_size:
            return self.get_by_order(node.left, k)
        elif k > left_size:
            return self.get_by_order(node.right, k - left_size - 1)
        else:
            return node.key

class AVLTreeWrapper:
    def __init__(self):
        self.root = None
        self.tree = AVLTree()

    def find(self, key):
        return self.tree.find(self.root, key)

    def insert(self, key):
        self.root = self.tree.insert(self.root, key)

    def remove(self, key):
        self.root = self.tree.delete(self.root, key)

    def order_of_key(self, key):
        return self.tree.order_of_key(self.root, key)

    def get_by_order(self, k):
        return self.tree.get_by_order(self.root, k)
