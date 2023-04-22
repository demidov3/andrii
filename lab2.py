def tsp(graph, start):
    path = [start]
    n = len(graph)
    visited = [False] * n
    visited[start] = True
    while len(path) < n:
        current = path[-1]
        min_dist = float('inf')
        next_node = None
        for i in range(n):
            if not visited[i] and graph[current][i] < min_dist:
                min_dist = graph[current][i]
                next_node = i
        path.append(next_node)
        visited[next_node] = True
    path.append(path[0])
    return path

graph = [[0, 0, 0, 0, 86, 94, 51, 82], [0, 0, 81, 0, 20, 87, 0, 0], [0, 81, 0, 83, 41, 0, 0, 0], [0, 0, 83, 0, 8, 0, 0, 0], [86, 20, 41, 8, 0, 40, 0, 54], [94, 87, 0, 0, 40, 0, 89, 0], [51, 0, 0, 0, 0, 89, 0, 18], [82, 0, 0, 0, 54, 0, 18, 0]]

start = 0
print(tsp(graph, start))
