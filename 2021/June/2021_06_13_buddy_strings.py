class Solution:
    # O(n) time complexity: len(strings) + one pass to fix or find duplicates
    # O(k) space complexity: seen set with max size 26
    def buddyStrings(self, A, B):
        lenA, lenB = len(A), len(B)
        if lenA != lenB: return False

        # swap with same letter, like ha1ba2 -> ha2ba1
        if A == B:
            seen = set()
            for a in A:
                if a in seen: return True
                seen.add(a)
            return False

        # swap to fix string
        mismatch, mismatches = [], 0
        for i in range(lenA):
            if A[i] != B[i]:
                if mismatches > 2: return False
                if mismatches == 1:
                    if mismatch[0][0] != B[i] or mismatch[0][1] != A[i]: return False
                mismatch.append((A[i], B[i]))
                mismatches += 1

        return mismatches == 2



print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
print(Solution().buddyStrings('aa', 'aa'))
# True
