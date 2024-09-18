from collections import deque

def bfs(source, sink, visited):
    q = deque()
    q.append(source)

    while q and visited[sink] == -1:
        u = q.popleft()
        for v in road[u]:
            if capacity[u][v] - flow[u][v] > 0 and visited[v] == -1:
                visited[v] = u
                if v == sink:
                    return False
                q.append(v)
                
    return True

def edmond_karp(source, sink):
    answer = 0
    
    while True:
        visited = [-1] * max_n
        min_flow = float('inf')
        
        if bfs(source, sink, visited):
            break
        
        v = sink
        while v != source + n + 1:
            u = visited[v]
            min_flow = min(min_flow, capacity[u][v] - flow[u][v])
            v = u
        
        v = sink
        while v != source + n + 1:
            u = visited[v]
            flow[u][v] += min_flow
            flow[v][u] -= min_flow
            v = u

        answer += min_flow
    
    return answer

n, p = map(int, input().split())
max_n = 2 * (n+1)

road = [[] for _ in range(max_n)]
capacity = [[0] * max_n for _ in range(max_n)]
flow = [[0] * max_n for _ in range(max_n)]

for i in range(p):
    u, v = map(int, input().split())
    u_in, u_out = u, u + n + 1
    v_in, v_out = v, v + n + 1
    
    road[u_out].append(v_in)
    road[v_in].append(u_out)
    road[v_out].append(u_in)
    road[u_in].append(v_out)

    capacity[u_out][v_in] = 1
    capacity[v_out][u_in] = 1
    
for i in range(1, n+1):
    u = i
    v = i + n + 1
    
    road[u].append(v)
    road[v].append(u)
    
    capacity[u][v] = 1
    
print(edmond_karp(1, 2))