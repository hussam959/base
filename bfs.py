def bfs(graph, start, goal):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adj_nodes = graph.get(node, [])
            for newnode in adj_nodes:
                newPath = path.copy()
                newPath.append(newnode)
                queue.append(newPath)
                

graph = {
    'S' : ['B','D','A'],
    'A': ['C'],
    'B': ['D'],
    'C':['G','D'],
    'D': ['G'],
}

sol = bfs(graph, 'S', 'G')
print(sol)

