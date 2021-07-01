class Solution:
    # O(n) time complexity: one pass through list to split, one to reverse substrings
    # O(n) space complexity: list of split substrings
    def reverseWords(self, str):
        return ' '.join([s[::-1] for s in str.split()])

print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
