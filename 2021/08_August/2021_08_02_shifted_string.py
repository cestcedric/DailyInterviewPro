# O(n^2) time: n tries, comparing strings in O(n), building shifted string O(n)
# O(n) space: shifted string of same size as b
def is_shifted_simple(a, b):
    if len(a) != len(b): return False

    for i in range(len(b)):
        if b[i:] + b[:i] == a: return True

    return False


# ---------------------------------------------------------------------------
# O(1) time: O(n) for initial hash, O(n) for each update
# O(1) space
class RollingHash:
    def __init__(self, str) -> None:
        self.MOD = 10 ** 9 + 7
        self.hash = 0
        self.window = len(str)
        
        for s in str:
            self.hash *= 10
            self.hash += ord(s)
            self.hash %= self.MOD

    
    def update(self, oldChar, newChar) -> None:
        self.hash -= ord(oldChar) * 10 ** (self.window - 1)
        self.hash *= 10
        self.hash += ord(newChar)
        self.hash %= self.MOD


# O(n) time: check all chars
# O(1) space
def compareOffset(a: str, b: str, o: int) -> bool:
    for i in range(len(a)):
        if a[i] != b[(i + o) % len(b)]: return False
    return True


# O(n) time: rolling hash in O(1), at most n tries
# O(1) space: rolling hash in constant space
def is_shifted(a: str, b: str) -> bool:
    if len(a) != len(b): return False
    
    goal = RollingHash(a)
    test = RollingHash(b)

    for i in range(len(b) - 2):
        test.update(b[i], b[i])
        if goal.hash == test.hash:
            if compareOffset(a, b, i + 1): return True
    
    return False


# ---------------------------------------------------------------------------
print(is_shifted('abcde', 'cdeab'))
# True
print(is_shifted('abc', 'acb'))
# False
print(is_shifted('gcmbf', 'fgcmb'))
# True
