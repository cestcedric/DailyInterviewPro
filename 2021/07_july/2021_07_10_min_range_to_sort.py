# Easy O(n * log(n)) solution: sort array, see when elements stop matching
# O(n) time complexity: push and pop each element at most twice
# O(n) space complexity: stacks with at most n elements
def findRange(nums):
    length = len(nums)
    if length == 1: return (0, 0)
    stack = []

    for n in nums:
        if stack == [] or stack[-1] <= n: stack.append(n)
        else:
            while stack[-1] > n: stack.pop()
            break

    start = len(stack)
    stack = []

    for n in nums[::-1]:
        if stack == [] or stack[-1] >= n: stack.append(n)
        else:
            while stack[-1] < n: stack.pop()
            break

    return (start, length - len(stack) - 1) 
    

print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
print(findRange([1,2,4,3,6,8,2,9,9,10,11]))
# (2, 6)
