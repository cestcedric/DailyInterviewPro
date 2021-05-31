class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next

def intersection(a, b):
    # O(n+m) time complexity, with len(a) = m and len(b) = m (dictionary lookup O(1))
    # O(n) space complexity
    seen = {}
    while a is not None:
        seen[id(a)] = None
        a = a.next
    while b is not None:
        if id(b) in seen: return b
        b = b.next
    return None

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4
