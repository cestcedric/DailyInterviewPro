class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# O(n) time complexity: looks once at each node
# O(log(n)) space complexity: call stack with max depth = height of tree
def count_unival_subtrees(root):
    if root is None: return 0
    count = 0

    def traverse(node):
        nonlocal count
        if node is None: return True
        if traverse(node.left) and traverse(node.right):
            if (node.left is None or node.left.val == node.val) and \
                (node.right is None or node.right.val == node.val):
                count += 1
                return True
        return False

    traverse(root)

    return count


a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print('Should be 5:', count_unival_subtrees(a))