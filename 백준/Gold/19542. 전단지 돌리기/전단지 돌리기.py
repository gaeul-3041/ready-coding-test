import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def DFS(cur, pre):
    global answer
    dist = 0
    for g in graph[cur]:
        if g != pre:
            dist = max(dist, DFS(g, cur))
    if dist >= d:
        answer += 1
    return dist + 1

n, s, d = map(int, input().split())
answer = 0
graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
DFS(s, 0)
print(max(0, 2*(answer-1)))