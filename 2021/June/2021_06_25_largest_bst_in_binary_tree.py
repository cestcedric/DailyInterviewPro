class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer

# O(n) time complexity: one DFS pass
# O(log(n)) space complexity: call stack depth
def largest_bst_subtree(root):
    if root is None: return None

    def dfs(node):
        if node is None: return True, None, None, None, 0
        subLeft = dfs(node.left)
        subRight = dfs(node.right)

        subTree = subLeft[0] and subRight[0] and \
            (subLeft[2] is None or node.key >= subLeft[2]) and \
            (subRight[1] is None or node.key <= subRight[1])

        if not subTree:
            if subLeft[4] > subRight[4]: return False, None, None, subLeft[3], subLeft[4]
            return False, None, None, subRight[3], subRight[4]
        
        return True, subLeft[1] or node.key, subRight[2] or node.key, node, max(subLeft[4], subRight[4]) + 1

    return dfs(root)[3]

#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(largest_bst_subtree(node))
#749
