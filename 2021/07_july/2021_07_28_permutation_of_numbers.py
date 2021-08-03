# O(n!) time complexity: number of possible permutations
# probably additionaly * n for list concatenation
# O(n!) space complexity: tmp with at most n! elements, output at second to last round with (n-1)! elements
def permuteUnique(nums: list):
    output = [[]]
        
    for n in nums:
        tmp = []
            
        for o in output:
            for i in range(len(o) + 1):
                tmp.append(o[:i] + [n] + o[i:])
                    
        output = tmp
            
    return output


def permute(nums):
    pass

print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
