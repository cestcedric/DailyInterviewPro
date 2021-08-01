from collections import defaultdict

# O(n) time complexity: 
# -> at most 2 * words nodes
# -> one pass through words to build graph
# -> one pass through graph for degree check
# -> one pass through graph for single component check
# O(n) space complexity: two sets and two dicts containing n nodes each
def chainedWords(words):
    graphIn = defaultdict(list)
    graphOut = defaultdict(list)
    nodes = set()
    visited = set()
    
    for w in words:
        nodes.add(w[0])
        nodes.add(w[-1])
        graphOut[w[0]].append(w[-1])
        graphIn[w[-1]].append(w[0])

    # in-degree == out-degree for each node
    for node in graphIn:
        if len(graphIn[node]) != len(graphOut[node]): return False

    # single component
    frontier = [words[0][0]]
    while frontier != []:
        nextFrontier = []
        for node in frontier:
            if node in visited: continue
            visited.add(node)
            nextFrontier.extend(graphOut[node])
        frontier = nextFrontier

    return nodes == visited



print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# True
print(chainedWords(['apple', 'avocado', 'snack', 'karat', 'tuna']))
# False