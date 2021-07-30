from collections import deque

class Node():
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

# O(n) time complexity: every node looked at once
# O(height) space complexity: call stack depth = tree height
def is_mirrored(x, y):
    if x is None and y is None: return True
    if x is None or y is None: return False
    if x.value != y.value: return False
    for a, b in zip(x.children, y.children[::-1]):
        if not is_mirrored(a, b): return False
    return True


# O(n) time complexity
# O(height) space complexity
def is_symmetric(root):
    if root is None: return True

    for x, y in zip(root.children, root.children[::-1]):
        if not is_mirrored(x, y): return False

    return True
    

tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree))
# True

tree = Node(4)
tree.children = [Node(3), Node(2)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree))
# False
