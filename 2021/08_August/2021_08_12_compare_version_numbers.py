class Solution:
    # O(n) time
    # O(n) space: for lists
    def compareVersion(self, version1, version2):
        list1, list2 = version1.split('.'), version2.split('.')
        
        list1.extend([0] * (len(list2) - len(list1)))
        list2.extend([0] * (len(list1) - len(list2)))
        
        for x, y in zip(list1, list2):
            if int(x) < int(y): return -1
            if int(x) > int(y): return 1
        return 0

version1 = "1.0.1"
version2 = "1"
print(Solution().compareVersion(version1, version2))
# 1
