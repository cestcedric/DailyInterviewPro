class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(2^(height+1)-1) time complexity: look at every node once
# O(height) space complexity: call stack depth
def valuesAtHeight(root, height):
    if root is None: return []
    if height == 1: return [root.value]
    return valuesAtHeight(root.left, height-1) + valuesAtHeight(root.right, height-1)


# O(2^(height+1)-1) time complexity
# O(2^height) space complexity: list containing references to the nodes (negligible probably)
def valuesAtHeightIt(root, height):
    if root is None: return []
    curr = [root]
    while curr != [] and height > 1:
        tmp = []
        height -= 1
        for node in curr:
            if node.left is not None: tmp.append(node.left)
            if node.right is not None: tmp.append(node.right)
        curr, tmp = tmp, []

    return [node.value for node in curr]

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeightIt(a, 3))
# [4, 5, 7]
