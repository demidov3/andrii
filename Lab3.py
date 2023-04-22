from typing import List, Tuple

def tsp(graph: List[List[int]]) -> Tuple[List[int], int]:
    n = len(graph)
    best_path = None
    best_cost = float('inf')

    def dfs(path, cost, visited):
        nonlocal best_path, best_cost
        if len(path) == n:
            cost += graph[path[-1]][path[0]]
            if cost < best_cost:
                best_cost = cost
                best_path = path
            return

        for i in range(n):
            if i not in visited:
                new_path = path + [i]
                new_cost = cost + graph[path[-1]][i]
                if new_cost < best_cost:
                    dfs(new_path, new_cost, visited | {i})

    for i in range(n):
        dfs([i], 0, {i})

    return best_path, best_cost

if __name__ == '__main__':
    graph = [
        [0, 0, 69, 60, 10, 20],
        [0, 0, 0, 31, 39, 2],
        [69, 0, 0, 0, 59, 0],
        [60, 31, 0, 0, 0, 36],
        [10, 39, 59, 0, 0, 79],
        [20, 2, 0, 36, 79, 0],
    ]
    path, cost = tsp(graph)
    print(f"Optimal path: {path}")
    print(f"Total cost: {cost}")