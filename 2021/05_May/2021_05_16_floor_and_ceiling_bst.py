class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    node = root_node

    while node:
        if node.value == k: return k, k
        if node.value < k:
            if floor is None: floor = node.value
            else: floor = max(floor, node.value)
            node = node.right
        if node.value > k:
            if ceil is None: ceil = node.value
            else: ceil = min(ceil, node.value)
            node = node.left
    
    return floor, ceil
                



def findCeilingFloorRec(root_node, k, floor=None, ceil=None):
    if root_node is None or floor == k and ceil == k: return floor, ceil

    # floor: biggest number <= k
    # if node.value > k => go left, if node.value < k go right
    # ceil: smallest number >= k
    # same, just backwards
    if root_node.value == k: return k, k
    elif root_node.value < k:
        if floor is None: floor = root_node.value
        else: floor = max(floor, root_node.value)
        floor, ceil = findCeilingFloorRec(root_node.right, k, floor, ceil)
    else:
        if ceil is None: ceil = root_node.value
        else: ceil = min(ceil, root_node.value)
        floor, ceil = findCeilingFloorRec(root_node.left, k, floor, ceil)

    return floor, ceil

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 5))
print(findCeilingFloorRec(root, 5))
# (4, 6)
