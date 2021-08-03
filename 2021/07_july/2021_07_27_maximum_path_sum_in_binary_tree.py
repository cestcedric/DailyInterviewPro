class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# O(n) time complexity: look at each node once
# O(h) space complexity: h = tree height
def maxPathSum(root: Node):

    def dfs(node: Node):
        if node is None: return 0, -1001
        
        # best paths in left and right subtree
        left_max_through_root, left_max = dfs(node.left)
        right_max_through_root, right_max = dfs(node.right)

        # best path including the current node,
        # might go from left to right subtree
        node_max_through_root = node.val + max(
            left_max_through_root + right_max_through_root,
            left_max_through_root,
            right_max_through_root,
            0)

        # overall best path in tree below node
        node_max = max(left_max, right_max, node_max_through_root)
        
        # best path including node and only one subtree
        # => can be continued in level above
        node_max_through_root_onesided = node.val + max(
            left_max_through_root,
            right_max_through_root,
            0
        )

        return node_max_through_root_onesided, node_max

    return max(dfs(root))


# (* denotes the max path)
#       *10
#       /  \
#     *2   *10
#     / \     \
#   *20  1    -25
#             /  \
#            3    4
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print(maxPathSum(root))
# 42
