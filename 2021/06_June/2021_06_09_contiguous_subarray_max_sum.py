# O(n) time complexity: iterate once over array
# O(1) space complexity: only need space for two additional variables
def max_subarray_sum(arr):
    best = -float('inf')
    curr = 0
    for n in arr:
        curr = max(n, curr+n)
        best = max(best, curr)
    return best

print('Should be 137: {}'.format(max_subarray_sum([34, -50, 42, 14, -5, 86])))

