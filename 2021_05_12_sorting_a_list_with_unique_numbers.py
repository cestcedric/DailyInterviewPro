def sortNums(nums):
    index1, i, index3 = 0, 0, len(nums) - 1
    while i <= index3:
        if nums[i] == 1:
            nums[i], nums[index1] = nums[index1], nums[i]
            index1 += 1
            i += 1
        elif nums[i] == 3:
            nums[i], nums[index3] = nums[index3], nums[i]
            index3 -= 1
        else:
            i += 1
    return nums


print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
