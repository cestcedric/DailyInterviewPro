def staircase(n):
    # 1 -> 1
    # 2 -> 2 or 1,1
    # 3 -> 2,1 or 1,2 or 1,(1,1)
    # O(n) time and space complexity
    steps = [1,2]
    for i in range(2, n):
        steps.append(steps[i-1] + steps[i-2])
    return steps[n-1]

def staircase2(n):
    # O(n) time complexity, O(k) space complexity
    if n in [1,2]: return n
    step_1 = 1
    step_2 = 2
    for i in range(2,n):
        step_1, step_2 = step_2, step_1 + step_2
    return step_2


  
print('Should be 2: {}'.format(staircase(2)))
print('Should be 3: {}'.format(staircase(3)))
print('Should be 5: {}'.format(staircase(4)))
print('Should be 8: {}'.format(staircase(5)))

print('Should be 2: {}'.format(staircase2(2)))
print('Should be 3: {}'.format(staircase2(3)))
print('Should be 5: {}'.format(staircase2(4)))
print('Should be 8: {}'.format(staircase2(5)))
