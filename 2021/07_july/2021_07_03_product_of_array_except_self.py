# O(n) time complexity: two passes through nums
# O(1) space complexity: not counting the output array
def products(nums):
    n = len(nums)
    result = [1 for n in nums]

    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    revProd = nums[-1]
    for i in range(n - 2, -1, -1):
        result[i] *= revProd
        revProd *= nums[i]

    return result

print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
