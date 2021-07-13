# O(n) time complexity
# O(1) space complexity, only output array created
def getBonuses(performance):
    n = len(performance)
    bonus = [1] * n

    for i in range(n - 1):
        if performance[i] > performance[i + 1]: bonus[i] += 1
        else: bonus[i + 1] += 1

    return bonus

print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]
