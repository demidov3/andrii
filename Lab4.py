from typing import List, Tuple

def find_max_flow(capacity: List[List[int]], source: int, sink: int) -> Tuple[int, List[List[int]]]:
    n = len(capacity)
    flow = [[0] * n for _ in range(n)]
    max_flow = 0
    
    while True:
        # Шукаємо шлях з джерела до стоку за допомогою BFS
        parent = [-1] * n
        parent[source] = source
        queue = [source]
        while queue and parent[sink] == -1:
            u = queue.pop(0)
            for v in range(n):
                if parent[v] == -1 and capacity[u][v] - flow[u][v] > 0:
                    parent[v] = u
                    queue.append(v)

        # Якщо шлях не знайдено, закінчуємо цикл
        if parent[sink] == -1:
            break

        # Знаходимо максимальний потік по знайденому шляху
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v] - flow[u][v])
            v = u

        # Оновлюємо потік
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u

        max_flow += path_flow

    return max_flow, flow

if __name__ == '__main__':
    capacity = [
        [0, 20, 20, 20, 0, 0, 0, 0],
        [0, 0, 0, 0, 30, 0, 0, 0],
        [0, 10, 0, 0, 0, 10, 20, 0],
        [0, 0, 0, 0, 0, 15, 0, 0],
        [0, 0, 10, 0, 0, 10, 0, 20],
        [0, 0, 0, 0, 0, 0, 10, 20],
        [0, 0, 0, 10, 0, 0, 0, 20],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    source = 0
    sink = 7
    max_flow, flow = find_max_flow(capacity, source, sink)
    print(f"Max flow: {max_flow}")
    print("Flow matrix:")
    for row in flow:
        print