# Definition for a linked-list node.
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, a, b):
        merged = Node(None)
        _a = a
        _b = b
        _m = merged
        while _a and _b:
            if _a.val < _b.val:
                _m.val = _a.val
                _a = _a.next
            else:
                _m.val = _b.val
                _b = _b.next
            _prev = _m
            _prev.next = Node(None)
            _m = _prev.next
        if _a == None:
            _prev.next = _b
        elif _b == None:
            _prev.next = _a
        return merged


    def mergeTwoListsReq(self, a, b):
        if a == None:
            return b
        if b == None:
            return a
        if a.val < b.val:
            merged = Node(a.val)
            merged.next = self.mergeTwoListsReq(a.next, b)
        else:
            merged = Node(b.val)
            merged.next = self.mergeTwoListsReq(a, b.next)
        return merged


# Test program
# 1 -> 3 ->5
a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

# 2 -> 4 -> 6
b = Node(2)
b.next = Node(4)
b.next.next = Node(6)

c = Solution().mergeTwoLists(a, b)
while c:
  print(c.val)
  c = c.next
# 1 2 3 4 5 6