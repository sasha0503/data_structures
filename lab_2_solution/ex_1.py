# Створення класу вузла для бінарного дерева
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Функція для вставки нового вузла в бінарне дерево
def insert_node(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert_node(root.left, value)
        else:
            root.right = insert_node(root.right, value)
    return root


# Функція для обходу дерева прямим способом (preorder)
def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)


# Функція для обходу дерева оберненим способом (postorder)
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')


# Функція для обходу дерева симетричним способом (inorder)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)


def print_tree(root, level=0):
    if root:
        print_tree(root.right, level=level + 1)
        print(' ' * 6 * level + '->', root.value)
        print_tree(root.left, level=level + 1)


# Заданий масив з 20 значень
array = [15, 10, 20, 8, 12, 17, 25, 6, 9, 11, 14, 16, 18, 23, 27, 5, 7, 13, 19, 22]

# Побудова бінарного дерева
root = None
for value in array:
    root = insert_node(root, value)

# Виведення побудованого дерева і результатів обходів
print("Побудоване бінарне дерево:")
preorder_traversal(root)
print("\n\nРезультат прямого обходу:")
preorder_traversal(root)
print("\n\nРезультат оберненого обходу:")
postorder_traversal(root)
print("\n\nРезультат симетричного обходу:")
inorder_traversal(root)

# Виведення дерева
print("\n\nВиведення дерева:")
print_tree(root)
