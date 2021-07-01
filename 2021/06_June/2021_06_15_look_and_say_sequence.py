from functools import lru_cache
# 1      #
# 11     # one 1's
# 21     # two 1's
# 1211   # one 2, and one 1.
# 111221 # #one 1, one 2, and two 1's.

# O(n*k) time complexity: cache obviously faster, but depends on earlier calls
# k = avg(len(output))
# O(n) space complexity: call stack
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


# O(n*k) time complexity: k is average length of outputs up to n
# k = avg(len(output))
# O(1) space complexity
def lookAndSayIt(n):
    output = '1'

    for _ in range(2, n+1):
        tmp = ''
        c, count = output[0], 1
        for d in output[1:]:
            if d == c: count += 1
            else:
                tmp += '{}{}'.format(count, c)
                c, count = d, 1
        tmp += '{}{}'.format(count, c)
        output = tmp

    return output


for i in range(1, 31):
    print(lookAndSay(i) == lookAndSayIt(i))

