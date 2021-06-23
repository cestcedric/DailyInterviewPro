class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


# O(n) time complexity, will reach all nodes
# O(log(n)) space complexity: call stack with maximum depth of height of the tree
def deepest(node):
    if node is None: return None, 0

    left = deepest(node.left)
    right = deepest(node.right)

    if left[1] > right[1]: 
        return left[0] if left[0] is not None else node, 1 + left[1] 
    return right[0] if right[0] is not None else node, 1 + right[1]

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)
