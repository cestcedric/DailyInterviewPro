# O(n*s*log(s)) time complexity: s = length of individual strings, groupMap with O(1) access
# O(n) space complexity: groupMap with at most n entries
def groupAnagramWords(strs):
    groupMap = {}
    anagrams, n = [], 0

    for str in strs:
        s = ''.join(sorted(str))
        if s in groupMap: anagrams[groupMap[s]].append(str)
        else:
            groupMap[s] = n
            anagrams.append([str])
            n += 1

    return anagrams



print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
