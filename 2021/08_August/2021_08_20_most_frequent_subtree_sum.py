from collections import defaultdict

class Node():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


# O(n) time: look at each node once, then one run through counts
# O(n) space: counts contains at most n entries, when no subtree sums repeat
def most_freq_subtree_sum(root):
    counts = defaultdict(int)

    def dfs(node: Node) -> int:
        nonlocal counts

        if node is None: return 0

        subtreeSum = node.val + dfs(node.left) + dfs(node.right)
        counts[subtreeSum] += 1
        return subtreeSum

    dfs(root)

    maxCount, maxSum = 0, []

    for subtreeSum, sumCount in counts.items():
        # return all subtree sums with max count, remove '==' case to only return one
        if sumCount == maxCount: maxSum.append(subtreeSum)
        elif sumCount > maxCount: 
            maxCount = sumCount
            maxSum = [subtreeSum]

    return maxSum





root = Node(3, Node(1), Node(-3))
print(most_freq_subtree_sum(root))
# 1
