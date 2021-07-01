class Solution:
  def lengthOfLongestSubstring(self, s):
    seen = {}
    maxLength = 0
    currentLength = 0
    for c in s:
        # lookup in dictionary usually with O(1) time complexity by hashing
        if c in seen:
            maxLength = max(maxLength, currentLength)
            currentLength = 1
            seen = {}
            seen[c] = None
        else:
            seen[c] = None
            currentLength += 1
    maxLength = max(maxLength, currentLength)
    return maxLength


testcases = [
    ('abc', 3),
    ('aabb', 2),
    ('aabcc', 3),
    ('abrkaabcdefghijjxxx', 10)
]

for s, n in testcases:
    l = Solution().lengthOfLongestSubstring(s)
    print('Length of longest substring w/o repetition in \'{}\': {}. Your solution: {}.'.format(s, n, l))
    assert l == n
