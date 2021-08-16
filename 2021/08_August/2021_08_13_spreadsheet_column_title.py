class Solution:
    # O(n) time: n = length of title
    # O(1) space: only space for output string needed
    def convertToTitle(self, n):
        alphabet = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        title = ''

        while n > 0:
            n, m =  divmod(n, 26)
            title += alphabet[m]
            if m == 0: n -= 1

        return title[::-1]

input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB
