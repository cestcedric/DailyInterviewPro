# O(n) time: traverse input string once
# O(1) space: counter for opened and closed brackets
def fix_brackets(s):
    OPEN, CLOSED = '(', ')'
    countOpen, countClosed = 0, 0

    for b in s:
        if b == OPEN: countOpen += 1
        elif b == CLOSED:
            if countOpen > 0: countOpen -= 1
            else: countClosed += 1
    
    return countOpen + countClosed

print(fix_brackets('(()()'))
# 1
print(fix_brackets('()()()'))
# 0
print(fix_brackets(')()()()('))
# 2
