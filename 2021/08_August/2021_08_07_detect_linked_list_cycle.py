class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # O(n) time: one pass through list
    # O(n) space: at most n elements in visited
    def hasCycleSet(self, head):
        visited = set()

        while head is not None:
            if id(head) in visited: return True
            visited.add(id(head))
            head = head.next

        return False


    # O(n) time: p2 passes through set twice to catch p1 from the back
    # O(1) space: only two pointers
    def hasCycle2Pointers(self, head):
        p1, p2 = head, head

        while True:
            for _ in range(2):
                if p2 is None: return False
                p2 = p2.next

            p1 = p1.next
            if p1 == p2: return True


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

print(Solution().hasCycle2Pointers(testHead))
# True
