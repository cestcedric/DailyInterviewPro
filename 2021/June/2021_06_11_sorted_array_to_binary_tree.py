from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer


# O(n) time complexity
# O(log(n)) space complexity: extra call stack for subtrees
def createBalancedBST(nums):
    n = len(nums)
    if n == 0: return None
    if n == 1: return Node(nums[0])
    i = n // 2
    root = Node(nums[i])
    root.left = createBalancedBST(nums[:i])
    root.right = createBalancedBST(nums[i+1:])
    return root


print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))
# 4261357
#   4
#  / \
# 2   6
#/ \ / \
#1 3 5 7
