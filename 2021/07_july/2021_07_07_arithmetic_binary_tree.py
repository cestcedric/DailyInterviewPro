class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

# O(n) time complexity: looks at each node once
# O(n) space complexity: call stack if tree in one line
def evaluate(root):
    if type(root.val) == int: return root.val
    if root.val == PLUS: return evaluate(root.left) + evaluate(root.right)
    if root.val == MINUS: return evaluate(root.left) - evaluate(root.right)
    if root.val == TIMES: return evaluate(root.left) * evaluate(root.right)
    if root.val == DIVIDE: return evaluate(root.left) / evaluate(root.right)

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))
# 45
