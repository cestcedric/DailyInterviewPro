from functools import lru_cache
# 1      #
# 11     # one 1's
# 21     # two 1's
# 1211   # one 2, and one 1.
# 111221 # #one 1, one 2, and two 1's.

@lru_cache()
def lookAndSay(n):
    if n == 1: return '1'

    output = ''
    prev = lookAndSay(n-1)
    c, count = prev[0], 1
    for d in prev[1:]:
        if d == c: count += 1
        else: 
            output += '{}{}'.format(count, c)
            c, count = d, 1
    output += '{}{}'.format(count, c)

    return output



for i in range(1, 6):
    print(lookAndSay(i))

