class Solution(object):
    # O(n^2) time complexity:
    # a passing through array from left to right
    # b and c cover rest together
    # O(1) space complexity: only output array and constant number of variables created
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        output = []
        if n < 3: return output

        prev_a = None
        for a in range(n-2):
            if nums[a] == prev_a: continue
            b = a + 1
            c = n - 1
            while b < c:
                s = nums[a] + nums[b] + nums[c]
                if s > 0: c -= 1
                elif s < 0: b += 1
                elif output == [] or output[-1] != [nums[a], nums[b], nums[c]]: 
                    output.append([nums[a], nums[b], nums[c]])
                    b, c = b + 1, c - 1
                else: b, c = b + 1, c - 1
            prev_a = nums[a]

        return output




# Test Program
nums = [-2,0,0,2,2]#[-1,0,1,2,-1,-4]#[1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]
