

def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost, path[-1][0]


def ucs(graph: dict, start: str, goal:str):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adj_nodes = graph.get(node, [])
            for (newnode, cost) in adj_nodes:
                newpath = list(path)
                newpath.append((newnode, cost))
                queue.append(newpath)
    
graph = {
    'S' : [('A', 2),('B', 3),('D', 5)],
    'A': [('C', 4)],
    'B': [('D', 4)],
    'C': [('D', 1),('G', 2)],
    'D': [('G', 5)],
}

sol = ucs(graph, 'S', 'G')
cost = path_cost(sol)
print(sol)
print(f"Cost = {cost[0]}")
