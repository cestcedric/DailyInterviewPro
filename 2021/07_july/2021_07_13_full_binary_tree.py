from collections import deque

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value
  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      num = len(q)
      while num > 0:
        n = q.popleft()
        result += str(n.value)
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
        num = num - 1
      if len(q):
        result += "\n"

    return result


# O(n) time complexity: look at each node once
# O(log(n)) space complexity: call stack with depth = height of tree,
# which is hopefully kinda balanced;
# O(n) space complexity if totally rubbish tree that's just a line
def fullBinaryTree(node):
    if node is None: return None
    if node.left is None and node.right is None: return node
    if node.left is None: return fullBinaryTree(node.right)
    if node.right is None: return fullBinaryTree(node.left)

    node.left = fullBinaryTree(node.left)
    node.right = fullBinaryTree(node.right)
    return node

# Given this tree:
#     1
#    / \ 
#   2   3
#  /   / \
# 0   9   4

# We want a tree like:
#     1
#    / \ 
#   0   3
#      / \
#     9   4

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)
print(fullBinaryTree(tree))
# 1
# 03
# 94
