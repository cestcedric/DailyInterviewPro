def witnesses(heights):
    # 'murder' happens to the right of the array => backwards traversal
    # O(n) time complexity (simple traversal)
    # O(k) memory complexity, just two additional variables needed
    witnesses = 0
    maxHeight = -1
    for h in heights[::-1]:
        if h > maxHeight: witnesses += 1
        maxHeight = max(maxHeight, h)
    return witnesses

print('Should be 3: {}'.format(witnesses([3, 6, 3, 4, 1])))
print('Should be 1: {}'.format(witnesses([3, 6, 3, 4, 8])))
print('Should be 4: {}'.format(witnesses([3, 6, 5, 4, 1])))
print('Should be 7: {}'.format(witnesses([7, 6, 5, 4, 3, 2, 1])))

