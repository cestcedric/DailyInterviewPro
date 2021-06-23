class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

# O(n) time complexity: look at every node once
# O(log(n)) space complexity: call stack depth = tree height
def is_bst(root):
    if root.left is None and root.right is None: return True
    
    def traverse(node):
        if node.left is None and node.right is None: return True, node.key, node.key

        if node.left is None:
            rightSub = traverse(node.right)
            if rightSub[0] and rightSub[1] > node.key: return True, node.key, rightSub[2]
            return False, 0, 0

        if node.right is None:
            leftSub = traverse(node.left)
            if leftSub[0] and leftSub[2] < node.key: return True, leftSub[1], node.key
            return False, 0, 0
        
        leftSub = traverse(node.left)
        rightSub = traverse(node.right)
        validSubs = leftSub[0] and rightSub[0]
        validValues = leftSub[2] < node.key and rightSub[1] > node.key
        return validSubs and validValues, leftSub[1], rightSub[2]

    return traverse(root)[0]

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))

#    5
#   / \
#  3   7
# / \ /
#1  4 6
