import heapq

def prim_mst(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    heap = []
    mst = []
    start_node = 0
    visited[start_node] = True
    
    for j in range(n):
        if adj_matrix[start_node][j] != 0:
            heapq.heappush(heap, (adj_matrix[start_node][j], start_node, j))
    
    while heap:
        (cost, frm, to) = heapq.heappop(heap)
        if visited[to]:
            continue
        visited[to] = True
        mst.append((frm, to, cost))
        
        for j in range(n):
            if adj_matrix[to][j] != 0 and not visited[j]:
                heapq.heappush(heap, (adj_matrix[to][j], to, j))
                
    return mst

adj_matrix = [
    [0, 0, 7, 0, 0, 0, 46, 98],
    [0, 0, 33, 0, 0, 99, 0, 0],
    [7, 33, 0, 99, 92, 28, 0, 64],
    [0, 0, 99, 0, 15, 52, 0, 0],
    [0, 0, 92, 15, 0, 0, 0, 58],
    [0, 99, 28, 52, 0, 0, 0, 0],
    [46, 0, 0, 0, 0, 0, 0, 36],
    [98, 0, 64, 0, 58, 0, 36, 0]
]

mst = prim_mst(adj_matrix)
print(mst)
