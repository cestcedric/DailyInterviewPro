from functools import lru_cache

# O(n^2) time complexity:
# worst case: for every entry, you can jump at best to n - 2
# => have to check every entry before coming to base case
# O(n) space complexity: call stack with depth at most n
def jumpToEndRecursion(nums):
    MAX_VALUE = 10 ** 5

    @lru_cache(None)
    def jumpRec(pos):
        nonlocal nums, MAX_VALUE
        if pos >= len(nums) - 1: return 0
        if nums[pos] == 0: return MAX_VALUE
        return 1 + min([jumpRec(pos + i) for i in range(1, nums[pos] + 1)])

    return jumpRec(0)

print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
# 2

print(jumpToEnd([1,2,3]))

print(jumpToEnd([2,3,0,1,4]))
