class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        t_a = target - 0.5
        t_b = target + 0.5

        p_a = self.binarySearch(nums, t_a)
        if p_a == -1 or p_a == len(nums) or nums[p_a] != target: return [-1,-1]
        p_b = self.binarySearch(nums, t_b) - 1
        return [p_a, p_b]


    def binarySearch(self, nums: list, target: int) -> int:
        length = len(nums)
        if length == 0:
            return -1
        if length == 1:
            if nums[0] < target:
                return 1
            return 0

        left = 0
        right = length - 1

        while left <= right:
            middle = (right + left) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return left


testcases = [
    ([5,7,7,8,8,10], 8, [3,4]),
    ([5,7,7,8,8,10], 6, [-1,-1]),
    ([], 0, [-1,-1]),
    ([1, 2, 2, 2, 2, 3, 4, 7, 8, 8] , 2, [1,4]),
    ([2,2], 3, [-1,-1])
]

for i, (nums, target, positions) in enumerate(testcases):
    result = Solution().searchRange(nums, target)
    print('Case #{} should be'.format(i+1), positions, 'is', result)
    assert positions == result
print('All test cases passed!')
        