from functools import lru_cache

# O(n^2) time complexity:
# worst case: for every entry, you can jump at best to n - 2
# => have to check every entry before coming to base case
# Caching reduces time complexity on average, but still O(n^2)
# O(n) space complexity: call stack with depth at most n, cache
def jumpToEndRecursion(nums):
    MAX_VALUE = 10 ** 5

    @lru_cache(None)
    def jumpRec(pos):
        nonlocal nums, MAX_VALUE
        if pos >= len(nums) - 1: return 0
        if nums[pos] == 0: return MAX_VALUE
        return 1 + min([jumpRec(pos + i) for i in range(1, nums[pos] + 1)])

    return jumpRec(0)



# O(n^2) time complexity: pretty much as recursive approach without caching
# O(n) space complexity: dp array with n entries
def jumpToEndDP(nums):
    MAX_VALUE = 10 ** 5
    n = len(nums)

    dp = [MAX_VALUE] * n
    dp[0] = 0

    for i in range(n):
        for j in range(i + 1, min(i + nums[i] + 1, n)):
            dp[j] = min(dp[j], dp[i] + 1)

    return dp[-1]


# O(n^2) time complexity: same as recursive approach with caching
# O(n) space complexity: obviously
def jumpToEndDPeff(nums):
    MAX_VALUE = 10 ** 5
    n = len(nums)

    dp = [MAX_VALUE] * n
    dp[n - 1] = 0

    for i in range(n - 2, -1, -1):
        if nums[i] > 0:
            dp[i] = 1 + min(dp[j] for j in range(i + 1, min(i + nums[i] + 1, n)))

    return dp[0]


print(jumpToEndDPeff([3, 2, 5, 1, 1, 9, 3, 4]))
# 2

print(jumpToEndDPeff([1,2,3]))

print(jumpToEndDPeff([2,3,0,1,4]))

print(jumpToEndDPeff([1,1,1,1]))
