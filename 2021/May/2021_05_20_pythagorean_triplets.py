def findPythagoreanTriplets(nums):
    # Overall time complexity O(n^2)
    squared = [ n**2 for n in nums ] # O(n)
    squared.sort() # O(n log(n))
    length = len(squared)

    if length < 3: return False

    # O(n^2)
    for i in range(length-1, 1, -1):
        j, k = 0, i-1
        while j < k:
            s = squared[i] - squared[j] - squared[k]
            if s < 0: k -= 1
            elif s > 0: j += 1
            else: return True
    return False



print('Should be True: {}'.format(findPythagoreanTriplets([3, 12, 5, 13])))
print('Should be True: {}'.format(findPythagoreanTriplets([1, 2, 3, 4, 5])))
print('Should be False: {}'.format(findPythagoreanTriplets([3, 17, 5, 13])))

