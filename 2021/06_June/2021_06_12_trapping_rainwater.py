# O(n^2) time complexity: iterate over array for each entry
# O(1) space complexity: only need a few additional variables
def capacity1(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        leftHeight, rightHeight = 0, 0
        x, y = i, i
        while x >= 0:
            leftHeight = max(leftHeight, arr[x])
            x -= 1
        while y < n:
            rightHeight = max(rightHeight, arr[y])
            y += 1
        total += max(min(leftHeight, rightHeight) - arr[i], 0)
    return total


# O(n) time complexity: two passes through arr
# O(n) space complexity: two additional lists of length n created
# Space needed can be reduce by 0.5 when directly performing filling computation 
def capacity2(arr):
    n = len(arr)
    fillFromLeft = [0 for _ in range(n)]
    fillFromRight = [0 for _ in range(n)]

    # highest walls on left side
    h = 0
    for i in range(n):
        fillFromLeft[i] = max(0, h - arr[i])
        if h < arr[i]: h = arr[i]

    # highest walls on right side
    h = 0
    for i in range(n-1, -1, -1):
        fillFromRight[i] = max(0, h - arr[i])
        if h < arr[i]: h = arr[i]

    # every basin has capacity of the lower wall
    total = 0
    for l, r in zip(fillFromLeft, fillFromRight):
        total += min(l, r)

    return total


# O(n) time complexity
# O(n) space complexity for stack
def capacity3(arr):
    n = len(arr)
    total = 0
    walls = []
    for i in range(n):
        if walls == []: 
            walls.append(i)
            continue
        while walls != [] and arr[walls[-1]] < arr[i]:
            h = walls.pop()
            if walls == []: continue
            nextH = walls[-1]
            d = i - nextH - 1
            total += d * (min(arr[i], arr[nextH]) - arr[h])
        walls.append(i)
    return total


# O(n) time complexity
# O(1) space complexity
def capacity(arr):
    n = len(arr)
    left, right = 0, n-1
    leftMax, rightMax = 0, 0
    total = 0

    while left < right:
        if arr[left] < arr[right]:
            if leftMax < arr[left]: leftMax = arr[left]
            else: total += leftMax - arr[left]
            left += 1
        else:
            if rightMax < arr[right]: rightMax = arr[right]
            else: total += rightMax - arr[right]
            right -= 1

    return total
        

print('Should be 6:', capacity([0,1,0,2,1,0,1,3,2,1,2,1]))
print('Should be 9:', capacity([4,2,0,3,2,5]))
