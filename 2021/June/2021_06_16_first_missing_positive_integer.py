# O(n) time complexity: one pass through nums, one pass through all possible numbers
# O(k) space complexity, if you convince someone that it is limited by the maximum of len(nums)
# O(n) space complexity, really
def first_missing_positive_set(nums):
    included = set(nums)
    for i in range(1, 2**31):
        if not i in included: return i


# O(n) time complexity: completely pass through nums, move every entry at most once
# O(1) space complexity: working on original list
def first_missing_positive(nums):
    length = len(nums)

    for i, n in enumerate(nums):
        if n < 1: 
            nums[i] = 0
            continue
        if n == i+1: 
            continue
        if n > length: 
            nums[i] = 0
            continue

        nums[i] = 0
        x, nums[n-1] = nums[n-1], n
        while x > 0 and not n == x:
            n = x
            if n > length: break
            x, nums[n-1] = nums[n-1], n


    for i, n in enumerate(nums):
        if n == 0: return i+1
    
    return i+2


    
        

print('Should be 2:', first_missing_positive([3, 4, -1, 1]))
print('Should be 3:', first_missing_positive([1,2,0]))
print('Should be 1:', first_missing_positive([7,8,9,11,12]))
print('Should be 2:', first_missing_positive([1]))
print('Should be 1:', first_missing_positive([-1]))
print('Should be 7:', first_missing_positive([1,2,6,3,5,4]))
print('Should be 2:', first_missing_positive([1,1]))
