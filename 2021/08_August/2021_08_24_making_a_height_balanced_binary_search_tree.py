class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        answer = str(self.value)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer

# O(n) time: no sorting or insertion needed, we know which element to use
# O(log(n)) space: call stack height = tree height = log(n), since balanced tree
def create_height_balanced_bst(nums):

    def helper(left, right):
        nonlocal nums
        if left == right: return None

        mid = (left + right) // 2
        node = Node(nums[mid])
        
        if mid > 0:
            node.left = helper(left, mid)
        if mid < right:
            node.right = helper(mid + 1, right)
        return node

    return helper(0, len(nums))

tree = create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
print(tree)
# 53214768
#  (pre-order traversal)
#       5
#      / \
#     3    7
#    / \  / \
#   2   4 6  8
#  /
# 1
