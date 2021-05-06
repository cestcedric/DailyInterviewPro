# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        val = c
        if l1 == None and l2 == None:
            if c > 0:
                return ListNode(c)
            else:
                return None
        if l1 != None:
            val += l1.val
            l1 = l1.next
        if l2 != None:
            val += l2.val
            l2 = l2.next
        out = ListNode(val % 10)
        out.next = self.addTwoNumbers(l1, l2, val // 10)
        return out



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8
