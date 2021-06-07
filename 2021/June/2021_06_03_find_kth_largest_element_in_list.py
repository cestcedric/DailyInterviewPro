# O(n log(n)) time complexity: sorting takes that time
# O(1) space complexity when sorting in-place, O(n) otherwise
def findKthLargest(nums, k):
    return sorted(nums)[-k]


print('Should be 5: {}'.format(findKthLargest([3, 5, 2, 4, 6, 8], 3)))

