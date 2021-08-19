# O(log10(n)) time and space: integer n has log10(n) digits
def is_palindrome(n):
    if n < 0: return False

    # get length
    digits, tmp = 0, n
    while tmp > 0:
        tmp //= 10
        digits += 1
    
    if digits == 1: return True

    # check if palindrome
    stack = []
    for _ in range(digits // 2):
        n, d = divmod(n, 10)
        stack.append(d)

    if digits % 2 == 1: n //= 10

    for _ in range(digits // 2):
        n, d = divmod(n, 10)
        if d == stack[-1]: stack.pop()
        else: return False

    return True


print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False
print(is_palindrome(1))
# True
print(is_palindrome(-1))
# False
