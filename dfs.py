def dfs(graph, start, goal):
    visited = []
    stack = [[start]]
    while stack:
        path = stack.pop()
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adj_nodes = graph.get(node, [])
            for newnode in adj_nodes:
                newpath = list(path)
                newpath.append(newnode)
                stack.append(newpath)
                
graph = {
    'S' : ['B','D','A'],
    'A': ['C'],
    'B': ['D'],
    'C':['G','D'],
    'D': ['G'],
}

sol = dfs(graph, 'S', 'G')
print(sol)
