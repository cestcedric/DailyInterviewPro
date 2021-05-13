def two_sum(nums, k):
    # use a dictionary to hash all values in one O(n) pass, look for 
    dic = {}
    for i in range(len(nums)):
        dic[nums[i]] = i
        c = k - nums[i]
        if c in dic and dic[c] != i: return True
    return False

print(two_sum([4,7,1,-3,2], 5))
# True
