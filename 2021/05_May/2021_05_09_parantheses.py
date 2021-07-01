class Solution:
    def isValid(self, s: str) -> bool:
        def match(p_open, p_close):
            if p_open == '(' and p_close == ')':
                return True
            if p_open == '[' and p_close == ']':
                return True
            if p_open == '{' and p_close == '}':
                return True
            return False
        buf = ''
        opening = ['(','[','{']
        closing = [')',']','}']
        for c in s:
            if c in opening:
                buf += c
            else:
                if buf == '':
                    return False
                else:
                    if match(buf[-1], c):
                        buf = buf[:-1]
                    else:
                        return False
        return buf == ''
        



# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = "]"
# should return False
print(Solution().isValid(s))
