class Solution():
    # O(n) time: one pass through array + concatenation of output lists
    # O(1) space: depending on how list concatenation is handled might also be O(n)
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            if carry == 0: break
        if carry == 1: return [carry] + digits
        else: return digits


print(Solution().plusOne([2, 9, 9]))
# [3, 0, 0]
print(Solution().plusOne([1, 4, 9, 9]))
# [1, 5, 0, 0]
print(Solution().plusOne([9, 9, 9]))
# [1, 0, 0, 0]
print(Solution().plusOne([0]))
# [1]
