# O(n) time complexity: 
# at most 2 * (n - 1) operations by treating first two entries with on comparison
# O(1) space complexity
def find_min_max(nums):
    # safety check, not necessary when assuming len(nums) >= 3
    if len(nums) == 1: return (nums[0], nums[0])

    if nums[0] < nums[1]:
        minValue, maxValue = nums[0], nums[1]
    else:
        minValue, maxValue = nums[1], nums[0]

    comparisons = 1
    for i in range(2, len(nums)):
        n = nums[i]
        if n >= maxValue:
            maxValue = n
            comparisons += 1
            continue
        if n < minValue:
            minValue = n
            comparisons += 2
            continue
        comparisons += 2

    print('Comparisons: {} of {}'.format(comparisons, 2 * len(nums) - 3))
    return (minValue, maxValue)


print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)
print(find_min_max([1,2,3,4,5,6,7,8]))
# (1, 8)
print(find_min_max([9,1,8,7,6,5,4,3,2]))
# (1, 9)
