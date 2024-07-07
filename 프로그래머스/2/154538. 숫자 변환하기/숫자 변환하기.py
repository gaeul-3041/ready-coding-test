from collections import deque

def solution(x, y, n):
    answer = -1
    
    q = deque()
    q.append((x, 0))
    visited = [0] * 1000001
    visited[x] = 1
    
    while q:
        t, step = q.popleft()
        if t > y:
            continue
        elif t == y:
            answer = step
            break
        for nx in [t + n, t * 2, t * 3]:
            if nx <= 1000000 and visited[nx] == 0:
                q.append((nx, step + 1))
                visited[nx] = 1
        
    return answer