from collections import deque

n = int(input())
graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
root = {}

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                root[i] = v
                
bfs(1)
ans = sorted(root.items(), key = lambda x : x[0])
for i in ans:
    print(i[1])