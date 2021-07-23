class Solution(object):
    # O(n) time complexity: look at each entry once
    # O(1) space complexity: limited by max integer value in Python for count
    def compress(self, chars):
        curr, count, index = chars[0], 1, 0

        def appendChar(c, count):
            nonlocal chars, index

            chars[index] = c
            index += 1

            if count > 1:
                count = str(count)
                for d in count:
                    chars[index] = str(d)
                    index += 1

        for i in range(1, len(chars)):
            c = chars[i]
            if c == curr:
                count += 1
            else:
                appendChar(curr, count)
                curr, count = c, 1

        appendChar(curr, count)

        return chars[:index]

print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']
