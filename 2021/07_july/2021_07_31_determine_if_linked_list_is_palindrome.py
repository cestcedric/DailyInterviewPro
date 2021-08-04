class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# ------------------------------------------------------------------------
# O(n) time complexity: start moves 0 -> n / 2, end moves 0 -> n -> n / 2
# O(1) space complexity
def is_palindrome(node: Node):
    start, end = node, node
    while end.next is not None: end = end.next

    while start != end and start != end.next:
        if start.val != end.val: return False
        start = start.next
        end = end.prev

    return True


# ------------------------------------------------------------------------
# O(n) time complexity: one pass to transform to array, array reversal
# O(n) space complexity: new array and reversed new array
def is_palindrome_single_linked(node: Node):
    array = []
    while node is not None:
        array.append(node.val)
        node = node.next

    return array == array[::-1]


# ------------------------------------------------------------------------
# O(n) time complexity
# O(1) space complexity
def is_palindrome_single_linked_constant_space(node: Node) -> bool:
    length = listLength(node)
    mid = accessListIndex(node, (length - 1) // 2)

    mid.next = reverse(mid.next)
    mid = mid.next

    while mid is not None:
        if node.val != mid.val: return False
        node = node.next
        mid = mid.next
    
    return True


# O(n) time
# O(1) space
def accessListIndex(node: Node, index: int) -> Node:
    while index > 0:
        if node is None: return None
        node = node.next
        index -= 1
    return node



# O(n) time
# O(1) space
def listLength(node: Node) -> int:
    length = 0
    while node is not None:
        length += 1
        node = node.next
    return length


# O(n) time complexity: one pass through list
# O(1) space complexity: only need one temp node
def reverse(node: Node) -> Node:
    prevNode, currNode = None, node

    while currNode is not None:
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode, currNode = currNode, nextNode

    return prevNode

# ------------------------------------------------------------------------
# Tests
node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('b')
node5 = Node('a')
node1.next, node2.prev = node2, node1
node2.next, node3.prev = node3, node2
node3.next, node4.prev = node4, node3
node4.next, node5.prev = node5, node4

node6 = Node('a')
node7 = Node('b')
node8 = Node('b')
node9 = Node('a')
node6.next, node7.prev = node7, node6
node7.next, node8.prev = node8, node7
node8.next, node9.prev = node9, node8

print(is_palindrome_single_linked_constant_space(node1))
# True

print(is_palindrome_single_linked_constant_space(node6))

print(is_palindrome_single_linked_constant_space(Node('a')))
