class Solution:
    # O(n) time complexity, iterate at most twice over nums (left + right)
    # O(k) space complexity, additional memory for total, left and best
    def minSubArrayLen(self, nums, s):
        if nums == []: return 0
        length = len(nums)

        best = length + 1
        left = 0
        total = 0
        for right in range(length):
            total += nums[right]
            while total >= s:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1

        if best > length: return 0
        else: return best

        

print('Should be 2: {}'.format(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7)))
print('Should be 1: {}'.format(Solution().minSubArrayLen([1, 4, 4], 4)))
print('Should be 0: {}'.format(Solution().minSubArrayLen([1, 1, 1, 1, 1, 1, 1], 11)))
print('Should be 5: {}'.format(Solution().minSubArrayLen([1, 2, 3, 4, 5], 15)))
print('Should be 2: {}'.format(Solution().minSubArrayLen([2, 3, 1, 1, 1, 1, 1], 5)))
