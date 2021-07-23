class Solution(object):
    # O(n) time complexity
    # O(1) space complexity
    def findSingle(self, nums):
        x = 0
        for n in nums:
            x ^= n
        return x

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3
