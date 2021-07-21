# O(n) time complexity: every subexpression evaluated once, then merged using stack
# O(n) space complexity: maximum stack height = no subexpressions = n
def decodeString(s):
    stack = []
    i = len(s) - 1
    
    while i >= 0:
        if s[i] == '[':
            substring = ''
            # get everything in parenthesis from stack
            while stack != [] and stack[-1] != ']':
                substring += stack.pop()
            # remove closing parenthesis
            stack.pop()
            i -= 1

            count = ''
            while i >= 0 and s[i].isdigit():
                count = s[i] + count
                i -= 1
            count = int(count)
            stack.append(substring * count)
        else:
            stack.append(s[i])
            i -= 1

    output = ''
    while stack != []:
        output += stack.pop()

    return output
    

print('Should be \'abbcabbc\': {}'.format(decodeString('2[a2[b]c]')))
print('Should be \'aaabcbc\': {}'.format(decodeString('3[a]2[bc]')))
print('Should be \'accaccacc\': {}'.format(decodeString('3[a2[c]]')))
print('Should be \'abcabccdcdcdef\': {}'.format(decodeString('2[abc]3[cd]ef')))
print('Should be \'abccdcdcdxyz\': {}'.format(decodeString('abc3[cd]xyz')))
