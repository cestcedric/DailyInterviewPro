def two_sum(nums, k):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k: return True
    return False

print(two_sum([4,7,1,-3,2], 5))
# True
