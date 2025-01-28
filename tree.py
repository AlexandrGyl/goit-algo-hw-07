class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left_child:
                self._insert(data, node.left_child)
            else:
                node.left_child = TreeNode(data)
        else:
            if node.right_child:
                self._insert(data, node.right_child)
            else:
                node.right_child = TreeNode(data)


# max value in tree 
    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.right_child:
            return self.get_max(node.right_child)
        return node.data

# min value in tree 
    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.left_child:
            return self.get_min(node.left_child)
        return node.data

# sum all values in tree

    def get_sum_value(self):
        if self.root:
            return self.get_sum(self.root)
        return 0

    def get_sum(self, node):
        if not node:
            return 0
        return node.data + self.get_sum(node.left_child) + self.get_sum(node.right_child)


bst = BinarySearchTree()
values = [10, 5, 15, 3, 7, 12, 18, 35, 44, 2, 25, 16]
for value in values:
    bst.insert(value)


max_value = bst.get_max_value()
print(f"Найбільше значення: {max_value}")


min_value = bst.get_min_value()
print(f"Найменше значення: {min_value}")


sum_value = bst.get_sum_value()
print(f"Сума всіх значень: {sum_value}")

