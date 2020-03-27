
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    def contains(self, target):
        if target == self.value:
            return True

        if target >= self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        if target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)

        if self.right is not None:
            self.right.for_each(cb)
        else:
            return None

    def in_order_print(self, node):
        if node.left is not None:
            node.left.in_order_print(node.left)

        print(node.value)
        if node.right is not None:
            node.right.in_order_print(node.right)

    def pre_order_dft(self, node):
        pass

    def post_order_dft(self, node):
        pass