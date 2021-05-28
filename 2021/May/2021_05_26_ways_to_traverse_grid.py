import math
import random

def num_ways_fact(n, m):
    # Problem: go right or down
    # Is the same as permutations of an array of 'r' and 'd'
    # n columns, m rows => n-1 steps to the right, m-1 steps down
    # fastest possible solution, because using maths
    # also, these functions are probably implemented in C, so pretty fast
    return (math.factorial(n+m-2) // (math.factorial(n-1)*math.factorial(m-1)))


def num_ways_dyn(n, m):
    # O(n*m) time and space complexity
    ways = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 1 or j == 1: ways[i][j] = 1
            else: ways[i][j] = ways[i-1][j] + ways[i][j-1]
    return ways[-1][-1]


def num_ways_dyn_eff(n, m):
    # Still O(n*m) time complexity
    # O(m) space complexity, as only current and last row of 'ways' relevant
    # For further optimization rotate matrix so for O(min(n,m)) space complexity
    ways = [[0 for _ in range(m+1)] for _ in range(2)]
    for i in range(n+1):
        _i = i % 2
        for j in range(m+1):
            if i == 1 or j == 1: ways[_i][j] = 1
            else: ways[_i][j] = ways[_i-1][j] + ways[_i][j-1]
    return ways[_i][-1]

for _ in range(1000):
    m = random.randint(1, 10)
    n = random.randint(1, 10)
    target = num_ways_fact(n, m)
    output_1 = num_ways_dyn(n, m)
    output_2 = num_ways_dyn_eff(n, m)
    assert target == output_2, 'n: {}, m: {} should lead to {}, but returned {}'.format(n, m, target, output_2)
print('All test cases passed!')


