def check(nums: list) -> bool:
    # O(n)
    # Two independent errors cannot be fixed with one change
    # One error can be fixed if at beginning or end, or removing if creates a valid array
    error = -1
    length = len(nums)
    for i in range(length - 1):
        if nums[i] > nums[i+1]:
            if error != -1: return False
            error = i

    if error in [-1, 0, length - 2]:
        return True
    if nums[error-1] <= nums[error+1] or nums[error] <= nums[error+2]:
        return True 

    return False

        


print(check([13,4,7]))
# True
print(check([5,1,3,2,5]))
# False
print(check([4,2,1]))
# False
print(check([-1,4,2,3]))
# True
