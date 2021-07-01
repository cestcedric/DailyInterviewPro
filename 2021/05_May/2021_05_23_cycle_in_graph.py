def find_cycle(graph):
    # O(n) time complexity (DFS visits each node at most once)
    # O(n) space complexity, 'visited' dict is at most as big as graph 
    def dfs(graph, visited):
        if graph == {}: return False
        queue = []
        for v in graph:
            if v in visited: return True
            queue.append(v)
            visited[v] = True
        for v in queue:
            if dfs(graph[v], visited): return True
        return False
    
    visited = {}
    return dfs(graph, visited)



graph = {
    'a': {'a2':{}, 'a3':{} },
    'b': {'b2':{}},
    'c': {}
}
print('Should be \'False\': {}'.format(find_cycle(graph)))
graph['c'] = graph
print('Should be \'True\': {}'.format(find_cycle(graph)))
