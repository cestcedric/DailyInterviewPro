from collections import defaultdict

class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value


# O(n * a) time: n nodes with a adjacent nodes, at most O(n * n)
# O(n) space: additional dict with number of adjacent nodes in original graph
def reverse_graph(graph):
    adjacencies = {node: len(node.adjacent) for node in graph.values()}

    for node in graph.values():
        print(node.value, '->', [a.value for a in node.adjacent], adjacencies[node])
        # notify adjacent nodes about change
        for i in range(adjacencies[node]):
            node.adjacent[i].adjacent.append(node)

        # this node's neighbours are notified, remove them
        node.adjacent = node.adjacent[adjacencies[node]:]

    return graph


a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

# c <- a -> b
# A         |
# |_________|

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

for _, val in reverse_graph(graph).items():
    print([a.value for a in val.adjacent])
# []
# ['a']
# ['a', 'b']
