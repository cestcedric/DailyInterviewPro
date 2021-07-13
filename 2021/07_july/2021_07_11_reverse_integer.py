class Solution:
    # O(n) time complexity, n = number of digits
    # O(1) space complexity
    def reverse(self, x):
        MAX_LIMIT, MAX_DIGIT = (2**31 - 1) // 10, 7
        MIN_LIMIT, MIN_DIGIT = (2**31) // 10, 8

        if -10 < x < 10: return x
        if x == -2**31 or x == 2**31 - 1: return 0

        reversed = 0
        if x < 0: sign, x = -1, -x
        else: sign = 1

        while x > 0:
            x, m = divmod(x, 10)
            if reversed > MIN_LIMIT or reversed == MIN_LIMIT and m > MIN_DIGIT:
                return 0
            if reversed > MAX_LIMIT or reversed == MAX_LIMIT and m > MAX_DIGIT:
                return 0

            reversed = 10 * reversed + m
        
        return sign * reversed


    # O(n) time complexity, even if string reversal looks like one op here
    # O(n) space complexity, since we create additional strings
    def reverseString(self, x):
        MAX_LIMIT = str(2**31 - 1)
        MIN_LIMIT = str(-2**31)

        if -10 < x < 10: return x

        if x < 0:
            reversed = '-' + str(x)[1:][::-1]
            if len(reversed) > len(MIN_LIMIT): return 0
            if len(reversed) == len(MIN_LIMIT) and reversed > MIN_LIMIT: return 0
            return int(reversed)
        else:
            reversed = str(x)[::-1]
            if len(reversed) > len(MAX_LIMIT): return 0
            if len(reversed) == len(MAX_LIMIT) and reversed > MAX_LIMIT: return 0
            return int(reversed)
        

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
print(Solution().reverse(-123))
# -321
print(Solution().reverse(32768))
# 86723
print(Solution().reverse(-2143847412))
