# O(n) time complexity: accessing each character at most twice
# O(k) space complexity: additional hashmap containing at most k entries
def longest_substring_with_k_distinct_characters(s, k):
    if s == '': return ''
    length = len(s)
    if length <= k: return s

    longestSub, maxLength = '', 0
    currSub, currLength = '', 0
    chars, numChars = {}, 0

    for c in s:
        print(currSub, chars)
        if c in chars:
            chars[c] += 1
        elif numChars < k:
            chars[c] = 1
            numChars += 1
        else:
            print(3, chars)
            if currLength > maxLength: longestSub, maxLength = currSub, currLength
            for i in range(currLength):
                d = currSub[i]
                chars[d] -= 1
                if chars[d] == 0:
                    numChars -= 1
                    currSub = currSub[i+1:]
                    currLength = currLength - i
                    break
            chars[c] = 1
            numChars += 1
        currSub += c
        currLength += 1

    if currLength > maxLength: return currSub
    return longestSub

print('Should be \'defff\':', longest_substring_with_k_distinct_characters('aabcdefff', 3))
print('Should be \'aaaaaaa\':', longest_substring_with_k_distinct_characters('aaaaaaa', 5))

