class Solution:
    # O(n) time complexity, moving elements at most once (assuming that index access of the list is O(1))
    # O(1) space complexity, operating on original list
    def moveZeroes(self, nums: list) -> None:
        numZeros = 0
        nonZero = 0

        for n in nums:
            if n == 0: numZeros += 1
            else:
                nums[nonZero] = n
                nonZero += 1

        for i in range(numZeros):
            nums[nonZero + i] = 0


testcases = [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0], [0]),
    ([0,0,0,2,0,1,3,4,0,0], [2,1,3,4,0,0,0,0,0,0])
]

for i, (input, target) in enumerate(testcases):
    Solution().moveZeroes(input)
    print('Case #{}: should be \n{}, is \n{}'.format(i+1, target, input))
        