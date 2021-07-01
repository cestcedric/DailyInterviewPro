import heapq

# O(n log(n)) time complexity: sorting takes that time
# O(1) space complexity when sorting in-place, O(n) otherwise
def findKthLargestSorted(nums, k):
    return sorted(nums)[-k]

# O(k log(n)) time complexity: O(n) for heapify, O(log(n)) for each heappop (k)
# O(n) space complexity for heap
def findKthLargest(nums, k):
    heap = [ -n for n in nums ]
    heapq.heapify(heap)
    for _ in range(k-1):
        heapq.heappop(heap)
    return - heapq.heappop(heap)


print('Should be 5: {}'.format(findKthLargest([3, 5, 2, 4, 6, 8], 3)))

