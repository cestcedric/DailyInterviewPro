class Solution:
    # O(n * log(n)) time complexity: sorting input arrays, then linear pass through them
    # O(1) space complexity: inplace sorting, additional space needed only for output array
    def intersection(self, nums1, nums2):
        # return list(set(nums1).intersection(nums2))
        nums1.sort()
        nums2.sort()

        m, n = len(nums1), len(nums2)

        i, j, intersection, lastElement = 0, 0, [], None
        while i < m and j < n:
            if nums1[i] < nums2[j]: 
                i += 1
                continue
            elif nums1[i] > nums2[j]: 
                j += 1
                continue
            elif nums1[i] != lastElement:
                intersection.append(nums1[i])
                lastElement = nums1[i]
            i += 1
            j += 1

        return intersection
        
        

            
        



print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]
print(Solution().intersection([1, 2, 2, 1], [2, 2]))
# [2]
