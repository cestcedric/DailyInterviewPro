def eval(expression: str) -> int:
    # O(n) time and space complexity
    # Heavy stack usage though, since all intermediate results are pushed again

    stack = []
    # we traverse character by character, so 345 = 3 * 10^2 + 4*10^1 + 5*10^0
    result = 0
    # add parentheses at the ends to terminate
    for c in '(' + expression + ')':
        # build number
        if c.isdigit(): result = result * 10 + int(c)
        # new subexpression: start with subresult 0
        elif c == '(':
            stack.append(0)
            stack.append('+')
            
        elif c != ' ':
            op = stack.pop()
            saved = stack.pop()
            if op == '+': result += saved
            else: result = saved - result

            if c == ')': continue
            stack.append(result)
            stack.append(c)
            result = 0
    return result



testcases = [
    ('- (3 + ( 2 - 1 ) )', -4),
    ('1 + 1', 2),
    (' 2-1 + 2 ', 3),
    ('(1+(4+5+2)-3)+(6+8)', 23),
    ('+48 + -48', 0)
]

for i, (input, target) in enumerate(testcases):
    output = eval(input)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert output == target
print('All test cases passed!')
        