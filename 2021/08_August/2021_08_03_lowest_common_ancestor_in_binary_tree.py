from functools import lru_cache

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val

# O(n) time: caching
# O(n) space: call stack depth = tree height
@lru_cache(None)
def dfs(root, node):
    if root is None: return False
    if root == node: return True
    return dfs(root.left, node) or dfs(root.right, node)


# O(n) time: caching, dfs will pass through each node at most once
# O(n) space: call stack depth = tree height
def lowestCommonAncestor(root, a, b):
    if root == a or root == b: return root

    aInLeft, aInRight = dfs(root.left, a), dfs(root.right, a)
    bInLeft, bInRight = dfs(root.left, b), dfs(root.right, b)

    # make sure that both nodes exist somewhere in tree, you never know
    if not ((aInLeft or aInRight) and (bInLeft or bInRight)): return None
    
    # check if in different branckes, otherwise go to subtree a and b are in
    if aInLeft != bInLeft: return root
    if aInLeft: return lowestCommonAncestor(root.left, a, b)
    else: return lowestCommonAncestor(root.right, a, b)


# O(n) time: at most n parent pointers to look at
# O(n) space: at most n parent pointers to store
def lowestCommonAncestorParentPointers(root: TreeNode, a: TreeNode, b: TreeNode) -> TreeNode:
    parentPointers = set()
    
    while a is not None:
        parentPointers.add(a.parent)
        a = a.parent

    while b is not None:
        if b in parentPointers: return b
        b = b.parent


#   a
#  / \
# b   c
#    / \
#   d*  e*
root = TreeNode('a')
root.left = TreeNode('b')
root.left.parent = root
root.right = TreeNode('c')
root.right.parent = root
a = root.right.left = TreeNode('d')
root.right.left.parent = root.right
b = root.right.right = TreeNode('e')
root.right.right.parent = root.right

print(lowestCommonAncestorParentPointers(root, a, b).val)
# c
