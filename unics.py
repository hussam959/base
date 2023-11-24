def ucs_cost(path):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    return g_cost, path[-1][0]

def aStar_cost(path):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    lastnode = path[-1][0]
    h_cost = H_TABLES[lastnode]
    f_cost = g_cost + h_cost
    return f_cost , lastnode
def ucs(graph: dict, start: str, goal: str):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=ucs_cost)
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
                newpath.append(newnode)
                queue.append(newpath)
graph = {
    'S': [('A', 2), ('B', 3), ('D', 5)],
    'A': [('C', 4)],
    'B': [('D', 4)],
    'C': [ ('D', 1),('G', 2)],
    'D': [('G', 5)]
}


H_TABLES = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}

sol = ucs(graph, 'S', 'G')
cost = ucs_cost(sol)
print(sol)
print(f"Cost = {cost[0]}")
