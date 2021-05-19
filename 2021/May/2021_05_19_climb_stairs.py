def staircase(n):
    # 1 -> 1
    # 2 -> 2 or 1,1
    # 3 -> 2,1 or 1,2 or 1,(1,1)
    # O(n) time and space complexity
    steps = [1,2]
    for i in range(2, n):
        steps.append(steps[i-1] + steps[i-2])
    return steps[n-1]

  
print('Should be 2: {}'.format(staircase(2)))
print('Should be 3: {}'.format(staircase(3)))
print('Should be 5: {}'.format(staircase(4)))
print('Should be 8: {}'.format(staircase(5)))
