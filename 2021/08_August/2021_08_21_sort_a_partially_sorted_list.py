import heapq

# O((k + n - k + k) * log(k)) = O((k + n) * log(k)) = O(n * log(k)) time
# assuming k <= n, presorted making no sense otherwise anyway
# O(k) space: heap with at most k elements
def sort_partially_sorted(nums, k):
    n = len(nums)
    heap = []

    # O(k * log(k)) time
    for i in range(k):
        heapq.heappush(heap, nums[i])

    # O((n - k) * log(k)) time
    for i in range(k, n):
        nums[i - k] = heapq.heappushpop(heap, nums[i])

    # O(k * log(k))
    for i in range(n - k, n):
        nums[i] = heapq.heappop(heap)

    return nums



print(sort_partially_sorted([3, 2, 6, 5, 4], 2))
# [2, 3, 4, 5, 6]
