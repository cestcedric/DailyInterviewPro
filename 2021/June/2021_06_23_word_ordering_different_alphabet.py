# O(n) time complexity: look at each word and character once, linear lookup in hashmap
# O(1) space complexity: hashmap of size 26 regardless of input
def isSorted(words, order):
    dictionary = {char: index for index, char in enumerate(order)}
    for x, y in zip(words[:-1], words[1:]):
        diff = False
        for c1, c2 in zip(x, y):
            if dictionary[c2] < dictionary[c1]:
                return False
            if dictionary[c2] > dictionary[c1]:
                diff = True
                break
        if not diff and len(y) < len(x): return False
    return True

    

print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"],"zyxwvutsrqponmlkjihgfedcba"))
# True
