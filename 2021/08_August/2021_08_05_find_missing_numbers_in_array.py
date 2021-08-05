class Solution(object):
    # O(n) time: two passes through array
    # O(1) space: only work on input array
    def findDisappearedNumbers(self, nums):
        for n in nums:
            n = abs(n)
            if nums[n - 1] > 0: nums[n - 1] *= -1

        notIncluded = []

        for i, n in enumerate(nums):
            if n > 0: notIncluded.append(i + 1)

        return notIncluded

nums = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumbers(nums))
# [3, 5]
print(Solution().findDisappearedNumbers([1,2,3,4,5]))
# []
