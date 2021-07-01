from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += str(n.val) + ' '
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result

# O(n) time complexity: create hashmap for inorder position of all nodes for constant access
# O(n) space complexity: n entries in hashmap
def reconstruct(preorder, inorder):
    rootNodes = {node: index for index, node in enumerate(inorder)}
    preorder_index = 0

    def construct(left, right):
        nonlocal inorder, preorder, preorder_index, rootNodes
        if left > right: return None

        root = Node(preorder[preorder_index])
        preorder_index += 1
        root.left = construct(left, rootNodes[root.val] - 1)
        root.right = construct(rootNodes[root.val] + 1, right)
        return root
        
    return construct(0, len(inorder) - 1)


print(reconstruct(preorder = ['a','b','d','e','c','f','g'], inorder = ['d','b','e','a','f','c','g']))
print(reconstruct(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))
print(reconstruct(preorder = [-1], inorder = [-1]))