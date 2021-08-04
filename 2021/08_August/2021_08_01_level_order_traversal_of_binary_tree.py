from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time complexity: deque has O(1) access to first element
# O(n) space complexity: deque
def print_level_order(root):
    if root is None: return

    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node.left is not None: queue.append(node.left)
        if node.right is not None: queue.append(node.right)
        
        print(node.val, end = '')
        if queue: print(' ', end = '')


root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
# 1 2 3 4 5
