class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


# O(n) time: look at each node once
# O(n) space: list with nodes in level
def minimum_level_sum(root):
    levelNodes, level = [root], 1
    minSum, minLevel = root.val + 1, 0

    while levelNodes != []:
        nextLevel = []
        levelSum = 0
        for node in levelNodes:
            levelSum += node.val
            if node.left is not None: nextLevel.append(node.left)
            if node.right is not None: nextLevel.append(node.right)

        if levelSum < minSum:
            minSum, minLevel = levelSum, level

        levelNodes = nextLevel
        level += 1

    return minSum


#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print(minimum_level_sum(node))
# 7
