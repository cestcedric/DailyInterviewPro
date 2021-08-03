# O(n) time complexity: visits at most all nodes twice
# O(n) space complexity: add at most n nodes to visited
def seqLength(predSuccDict, visited, n):
    if not (predSuccDict[n]['succ'] or predSuccDict[n]['pred']): return 1

    # find beginning
    while predSuccDict[n]['pred']: 
        n -= 1
        visited.add(n)
    minValue = n

    # find end
    while predSuccDict[n]['succ']:
        n += 1
        visited.add(n)
    maxValue = n

    return maxValue - minValue + 1


# O(n) time complexity: every sequence looked at once in the second part
# => overall O(n) elements inspected
# O(n) space complexity: predSuccDict and visited set
def longest_consecutiveDict(nums):
    predSuccDict = {}

    # n * O(1)
    for n in nums:
        pred, succ = False, False
        if n - 1 in predSuccDict:
            predSuccDict[n - 1]['succ'] = True
            pred = True
        if n + 1 in predSuccDict:
            predSuccDict[n + 1]['pred'] = True
            succ = True
        predSuccDict[n] = {'pred': pred, 'succ': succ}

    visited = set()
    maxLength = 0

    # skip visited nodes, every sequence visited once
    for n in predSuccDict:
        if n in visited: continue
        visited.add(n)
        maxLength = max(maxLength, seqLength(predSuccDict, visited, n))

    return maxLength


# O(n) time complexity: look at each element at most twice
# O(n) space complexity: create set from list
def longest_consecutive(nums: list) -> int:
    nums = set(nums)
    maxLength = 0

    for n in nums:
        if n - 1 in nums: continue

        length = 1
        while n + 1 in nums:
            n += 1
            length += 1
        
        maxLength = max(maxLength, length)

    return maxLength


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4
print(longest_consecutive([3,1,2]))
# 3
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))
# 9