# O(n) time complexity
# O(1) space complexity
class Solution():
    romanToDigit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    def romanToInt(self, s):
        total = 0

        prev = None
        for r in s:
            total += self.romanToDigit[r]
            if prev is not None and self.romanToDigit[prev] < self.romanToDigit[r]:
                total -= 2 * self.romanToDigit[prev]
            prev = r

        return total



    




    
n = 'MCMX'
print(Solution().romanToInt(n))
# 1910
