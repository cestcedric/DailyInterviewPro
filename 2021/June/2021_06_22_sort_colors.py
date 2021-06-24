class Solution:
    # O(n) time complexity: look at each entry once
    # O(1) space complexity: only three extra variables needed
    def sortColors(self, nums):
        next0, next2 = 0, len(nums) - 1
        i = 0
        while i <= next2:
            if nums[i] == 0:
                nums[next0], nums[i] = nums[i], nums[next0]
                next0 += 1
                i += 1
            elif nums[i] == 2:
                nums[next2], nums[i] = nums[i], nums[next2]
                next2 -= 1
            else: i += 1


nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
