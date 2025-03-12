from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n + 1):
    graph[i].sort()
    
def dfs(v):
    visited[v] = 1
    print(v, end = ' ')
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                
dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)