# O(n) time complexity, where n is not length of input, but position n fibonacci seq
# O(1) space complexity
class Solution():
    def fibonacci(self, n):
        x, y = 0, 1

        for _ in range(n):
            x, y = y, x + y

        return x

print(Solution().fibonacci(9))
# 34
print(Solution().fibonacci(10))
# 55
print(Solution().fibonacci(0))
# 0
print(Solution().fibonacci(1))
# 1
