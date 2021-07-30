from bisect import bisect_left
from collections import Counter

# O(n^2) time complexity: insert into heap takes O(n) at worst
# -> probably better with sorted list, but more with technical tricks
# O(n) space complexity: heap and output of length <= n
def rearrangeString(s):
    # O(n)
    counter = Counter(s)
    heap = [(counter[char], char) for char in counter]

    # O(n * log(n))
    heap.sort(key = lambda entry : entry[0])
    output = []

    # O(n)
    while heap != []:
        # O(1)
        count, char = heap.pop()
        if output != [] and char == output[-1]: 
            if len(heap) == 0: return ''
            heap.append((count, char))
            count, char = heap.pop(-2)
        output.append(char)
        if count > 1:
            # O(log(n))
            index = bisect_left(heap, (count - 1, ''))
            # O(n)
            heap.insert(index, (count - 1, char))

    return ''.join(output)


print(rearrangeString('abbccc'))
print(rearrangeString('abc'))
print(rearrangeString('aab'))
print(rearrangeString('aa'))
print(rearrangeString('a'))
print(rearrangeString('vvvlo'))