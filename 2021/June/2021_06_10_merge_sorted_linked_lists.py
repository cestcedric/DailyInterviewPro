import heapq

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

# O(n*l^2) time complexity: l lists of average length n
# O(1) time complexity, we only work with already present nodes and rearrange
def merge(lists):
    # check if any list is not None = last element reached
    def empty(lists):
        for l in lists:
            if l is not None: return False
        return True

    length = len(lists)
    if empty(lists): return None

    # clear empty lists
    toDelete = []
    offDelete = 0
    for l in range(length):
        if lists[l] is None: toDelete.append(l)
    for l in toDelete:
        lists.pop(l - offDelete)
        length -= 1
        offDelete += 1
    
    merged = None
    node = None
    while not empty(lists):
        _min = lists[0].val
        _minIndex = 0
        for l in range(1, length):
            if lists[l].val < _min:
                _min = lists[l].val
                _minIndex = l
        if merged is None: 
            merged = lists[_minIndex]
            node = merged
        else:
            node.next = lists[_minIndex]
            node = node.next
        if lists[_minIndex].next is None: 
            lists.pop(_minIndex)
            length -= 1
        else: lists[_minIndex] = lists[_minIndex].next
    return merged

# O(n*l) time complexity: look at each node twice (l lists, average length n)
# O(n*l) space complexity: create new node for each input node
def mergeHeap(lists):
    heap = []
    heapq.heapify(heap)
    for l in lists:
        node = l
        while node is not None: 
            heapq.heappush(heap, node.val)
            node = node.next

    if not heap: return None

    merged = Node(heapq.heappop(heap))
    node = merged
    while heap:
        node.next = Node(heapq.heappop(heap))
        node = node.next
    return merged



a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
c = Node(6, Node(7, Node(8)))
print('Should be 123456: {}'.format(mergeHeap([a, b])))
a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
c = Node(6, Node(7, Node(8)))
print('Should be 123456678: {}'.format(mergeHeap([a, b, c])))
print('Should be None: {}'.format(mergeHeap([])))
a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
c = Node(6, Node(7, Node(8)))
print('Should be 123456: {}'.format(mergeHeap([a, None, None, b])))
