class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)

def remove_kth_from_linked_list(head, k):
    # O(n) time complexity: every node looked at most thrice
    # O(k) space complexity, memory used for additional references to at most three nodes
    lookahead = head
    node = head
    for _ in range(k): lookahead = lookahead.next
    while lookahead is not None:
        lookahead = lookahead.next
        prev = node
        node = node.next
    if node == head: return head.next
    prev.next = node.next
    return head

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print('Should be [1, 2, 3, 4, 5]: {}'.format(head))
head = remove_kth_from_linked_list(head, 3)
print('Should be [1, 2, 4, 5]: {}'.format(head))
