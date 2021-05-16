class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    pass
                



def findCeilingFloorRec(root_node, k, floor=None, ceil=None):
    if root_node is None: return None, None
    if root_node.value <= k:
        print('Found {}'.format(root_node.value))
        if floor is None: floor = root_node.value
        else: floor = max(floor, root_node.value)
    if root_node.value >= k:
        if ceil is None: ceil = root_node.value
        else: ceil = min(ceil, root_node.value)

    left = findCeilingFloorRec(root_node.left, k, floor, ceil)
    right = findCeilingFloorRec(root_node.right, k, floor, ceil)
    
    if floor is not None:
        if left[0] is not None: floor = max(floor, left[0])
        if right[0] is not None: floor = max(floor, right[0])
    else:
        if left[0] is not None and right[0] is not None: floor = max(left[0], right[0])
        elif left[0] is None: floor = right[0]
        else: floor = left[0]

    if ceil is not None:
        if left[1] is not None: ceil = min(ceil, left[1])
        if right[1] is not None: ceil = min(ceil, right[1])
    else:
        if left[1] is not None and right[1] is not None: ceil = min(left[1], right[1])
        if left[1] is None: ceil = right[1]
        else: ceil = left[1]

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
