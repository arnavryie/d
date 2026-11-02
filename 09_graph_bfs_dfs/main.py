locations = ["A", "B", "C", "D", "E"]
n = len(locations)
loc_to_idx = {locations[i]: i for i in range(n)}

adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

adj_list = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B", "E"],
    "E": ["B", "C", "D"]
}

def dfs_matrix(start_node):
    visited = [False] * n
    res = []

    def dfs(u):
        visited[u] = True
        res.append(locations[u])
        for v in range(n):
            if adj_matrix[u][v] == 1 and not visited[v]:
                dfs(v)

    dfs(loc_to_idx[start_node])
    return res

def bfs_list(start_node):
    visited = {loc: False for loc in locations}
    queue = [start_node]
    visited[start_node] = True
    res = []

    while queue:
        curr = queue.pop(0)
        res.append(curr)
        for neighbor in adj_list.get(curr, []):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return res

print("Locations:", locations)
start = "A"

print(f"\nDFS Traversal (using Adjacency Matrix) starting from {start}:")
print(" -> ".join(dfs_matrix(start)))

print(f"\nBFS Traversal (using Adjacency List) starting from {start}:")
print(" -> ".join(bfs_list(start)))
