class Solution:
    # O(n^2) time complexity: check all previous entries for each entry
    # O(n) space complexity: dp of size of nums
    def lengthOfLIS(self, nums: list) -> int:
        n = len(nums)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + 1 if nums[j] < nums[i] else 1)

        return max(dp)




print('Should be 4:', Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print('Should be 4:', Solution().lengthOfLIS([0,1,0,3,2,3]))
print('Should be 1:', Solution().lengthOfLIS([7,7,7,7,7,7,7]))
        