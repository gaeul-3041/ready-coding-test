from collections import deque

answer = [-1, 0, 0, 0]
start = [[] for i in range(1000001)]
end = [[] for i in range(1000001)]
visited = [0 for i in range(1000001)]

def bfs(p):
    q = deque([p])
    visited[p] = 1

    while q:
        n = q.popleft()
        if len(start[n]) == 0:
            answer[2] += 1
            return
        if len(start[n]) == 2 and len(end[n]) == 2:
            answer[3] += 1
            return
        for i in start[n]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

    answer[1] += 1

def solution(edges):
    for s, e in edges:
        start[s].append(e)
        end[e].append(s)

    for i in range(1000001):
        if len(start[i]) >= 2 and len(end[i]) == 0:
            answer[0] = i
            visited[i] = 1
            break

    sp = answer[0]

    for p in start[sp]:
        end[p].remove(sp)
        bfs(p)

    return answer