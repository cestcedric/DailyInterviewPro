# O(n * log(n)) time complexity: sorting
# can use binary search for finding h, but doesn't matter in complexity
# O(1) space complexity: depending on sort algorithm
def hIndex(publications):
    publications.sort(reverse = True)

    if publications[0] == 0: return 0
    if len(publications) == 1: return 1
        
    for h in range(1, len(publications)):
        if publications[h - 1] >= h and publications[h] <= h:
            return h
            
    return h + 1



    



print(hIndex([5, 3, 3, 1, 0]))
# 3
print(hIndex([3,0,6,1,5]))
# 3
print(hIndex([1,3,1]))
# 1
print(hIndex([3,5]))
# 2
print(hIndex([0,0]))
# 0
print(hIndex([1,1,1,1,1]))
# 1
print(hIndex([34]))
# 1