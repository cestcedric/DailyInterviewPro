from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # O(n) time: look at each node once
    # O(n) space: at most n / 4 nodes in frontier and n / 2 in nextLevel
    def __str__(self):
        output = ''
        frontier = [self]

        while frontier != []:
            nextLevel = []
            for node in frontier:
                output += str(node.val)
                if node.left is not None: nextLevel.append(node.left)
                if node.right is not None: nextLevel.append(node.right)
            output += '\n'
            frontier = nextLevel

        return output




tree = Node('a')
tree.left = Node('b')
tree.right = Node('c')
tree.left.left = Node('d')
tree.left.right = Node('e')
tree.right.left = Node('f')
tree.right.right = Node('g')

print(tree)
# a
# bc
# defg
