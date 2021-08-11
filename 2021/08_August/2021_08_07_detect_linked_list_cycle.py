class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # O(n) time
    # O(n) space
    def hasCycle(self, head):
        visited = set()

        while head is not None:
            if id(head) in visited: return True
            visited.add(id(head))
            head = head.next

        return False


testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail
testTail.next = node1

print(Solution().hasCycle(testHead))
# True
