class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

# O(n * log(n)) time complexity: sorting
# O(n) space complexity: additional array with string numbers
def largestNum(nums):
    numStrings = [str(n) for n in nums]
    numStrings.sort(key = LargerNumKey)
    if numStrings[0] == '0': return '0'
    return ''.join(numStrings)




print(largestNum([17, 7, 2, 45, 72]))
# 77245217
print(largestNum([432, 43243]))
# 43243432
