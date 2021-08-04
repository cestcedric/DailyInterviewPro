# O(n) time complexity: one pass for cumulative sum, one to find edges
# O(n) space complexity: additional cumulative sum array
def find_continuous_k(nums, k):
    cumSum = [0]
    for n in nums: cumSum.append(cumSum[-1] + n)

    left, right = 0, 1
    while right <= len(nums):
        intervalSum = cumSum[right] - cumSum[left]
        if intervalSum == k and left < right: return nums[left:right]
        if intervalSum > k: left += 1
        else: right += 1

    return None


print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]
print(find_continuous_k([1, 4, 20, 3, 10, 5], 33))
# [20, 3, 10]
print(find_continuous_k([1, 4, 0, 0, 3, 10, 5], 7))
# [4, 0, 0, 3]
print(find_continuous_k([1, 2, 3], 0))
# None