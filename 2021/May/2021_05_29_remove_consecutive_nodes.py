class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def removeConsecutiveSumTo0(node):
    # O(n) time complexity: looking at each node at most twice (add + delete)
    # O(n) space complexity: hashmap contains at most all nodes once
    if node is None: return None

    sums = {}
    total = 0
    sums[0] = Node(0, node)

    while node is not None:
        total += node.value

        if total in sums:
            # found node balancing total
            # remove all nodes up to that
            tmp = sums[total].next
            tmp_total = total
            while tmp != node:
                tmp_total += tmp.value
                del(sums[tmp_total])
                tmp = tmp.next
            sums[total].next = node.next
        else:
            sums[total] = node
        node = node.next
    return sums[0].next



node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
print('Should be 10:')
while node:
    print(node.value)
    node = node.next

# 10
