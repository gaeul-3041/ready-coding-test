from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r, c, land, visited):
    n = len(land)
    m = len(land[0])
    
    q = deque()
    q.append((r, c))
    oils = [[r, c]]
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                oils.append([nx, ny])
                visited[nx][ny] = 1
                cnt += 1
                
    minY = m
    maxY = -1
    
    for i, j in oils:
        minY = min(minY, j)
        maxY = max(maxY, j)
        
    return minY, maxY, cnt

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[0] * m for i in range(n)]
    result = [0] * m
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                minY, maxY, cnt = bfs(i, j, land, visited)
                for k in range(minY, maxY + 1):
                    result[k] += cnt
    
    return max(result)