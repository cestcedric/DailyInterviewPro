# O(n) time complexity: one pass throught nums, one pass through ranges
# O(1) space complexity: O(n) if you count the output array
def findRanges(nums):
    if nums == []: return []
    ranges, r = [[]], 1

    for n in nums:
        if ranges[-1] == []: ranges[-1] = [n, n]
        elif ranges[-1][1] >= n - 1: ranges[-1][1] = n
        else: 
            ranges.append([n, n])
            r += 1

    for i in range(r):
        ranges[i] = '{}->{}'.format(ranges[i][0], ranges[i][1])

    return ranges



print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']
