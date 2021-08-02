# O(n) time complexity
# O(1) space complexity
# Concept: assuming we can create all numbers < smallest and are at nums[i]
# -> a) nums[i] > smallest => unable to build smallest
# -> b) nums[i] <= smallest: since we can build 1, 2, ..., smallest - 1 we can add
# nums[i] and remove 1, 2, ... to build all numbers in [smallest, smallest + nums[i]]
def findSmallest(nums):
    smallest = 1
    for n in nums:
        if n > smallest: return smallest
        smallest += n

print(findSmallest([1, 2, 3, 8, 9, 10]))
# 7
print(findSmallest([1, 1, 3, 8, 9, 10]))
# 6
