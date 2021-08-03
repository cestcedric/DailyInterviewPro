from collections import Counter

# O(n!) time complexity: number of possible permutations
# probably additionaly * n for list concatenation
# O(n!) space complexity: tmp with at most n! elements, output at second to last round with (n-1)! elements
# Easy way to adapt this solution to work for repeated elements: use tuples and set
def permuteUnique(nums: list):
    output = [[]]
        
    for n in nums:
        tmp = []
            
        for o in output:
            for i in range(len(o) + 1):
                tmp.append(o[:i] + [n] + o[i:])
                    
        output = tmp
            
    return output

# O(n!) time complexity: again additional * n included
# O(n) space complexity: call stack depth at most n for one permutation
def permute(nums):
    counter = Counter(nums)
    output = []
    n = len(nums)

    def dfs(sequence):
        nonlocal counter, output, n
        if len(sequence) == n: 
            output.append(sequence[::])
            return
        
        for c in counter:
            if counter[c] == 0: continue
            counter[c] -= 1
            sequence.append(c)
            dfs(sequence)
            sequence.pop()
            counter[c] += 1

    dfs([])
    return output

    

# print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
perm = permute([2,2,1,1])
for p in perm:
    print(p)
