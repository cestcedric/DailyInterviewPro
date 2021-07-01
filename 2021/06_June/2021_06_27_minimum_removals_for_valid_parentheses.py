# O(n) time complexity: one pass through string
# O(1) space complexity: only need two variables, regardless of string length
def count_invalid_parenthesis(string):
    count_open, count_close = 0, 0

    for s in string:
        if s == '(': count_open += 1
        elif count_open > 0: count_open -= 1
        else: count_close += 1

    return count_close + count_open


print('Should be 1:', count_invalid_parenthesis('()())()'))
print('Should be 2:', count_invalid_parenthesis(')('))