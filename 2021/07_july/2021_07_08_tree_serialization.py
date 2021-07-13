class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    # pre-order printing of the tree.
    result = ''
    result += str(self.val)
    if self.left:
      result += str(self.left)
    if self.right:
      result += str(self.right)
    return result

# O(n) time complexity
# O(log(n)) space complexity: call stack
def serialize(root):
    if root is None: return '#'
    else: return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

# O(n) time complexity
# O(log(n)) space complexity: references to nodes in stack
def serializeIt(root):
    if root is None: return '#'
    s, stack = '', [root]
    
    while stack != []:
        node = stack.pop()
        if node is None: s += ' #'
        else:
            s += ' {}'.format(node.val)
            stack.append(node.right)
            stack.append(node.left)

    return s.strip()


# O(n) time complexity
# O(n) space complexity by spliting string into list,
# can be avoided by e.g. not putting whitespace into the serialized string
def deserialize(data):
    if data[0] == '#': return None
    data = data.split(' ')

    def desRec(node, pos):
        nonlocal data
        leftPos = pos + 1
        if data[leftPos] == '#': rightPos = leftPos + 1
        else:
            node.left = Node(data[leftPos])
            rightPos = desRec(node.left, leftPos)

        if data[rightPos] == '#': return rightPos + 1
        else:
            node.right = Node(data[rightPos])
            return desRec(node.right, rightPos)

    root = Node(int(data[0]))
    desRec(root, 0)
    
    return root


#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print(serializeIt(tree))
# 1 3 2 # # 5 # # 4 # 7 # #
print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
# 132547
