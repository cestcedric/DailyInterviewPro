# O(n) time: n tries, comparing strings in O(n), building shifted string O(n)
# O(n) space: shifted string of same size as b
def is_shifted_simple(a, b):
    if len(a) != len(b): return False

    for i in range(len(b)):
        if b[i:] + b[:i] == a: return True

    return False

  
print(is_shifted_simple('abcde', 'cdeab'))
# True
print(is_shifted_simple('abc', 'acb'))
# False
