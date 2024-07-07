from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    road1, road2 = 0, 0
    sx, sy = 0, 0
    lx, ly = 0, 0
    ex, ey = 0, 0
    n, m = len(maps), len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'L':
                lx, ly = i, j
            elif maps[i][j] == 'E':
                ex, ey = i, j
            elif maps[i][j] == 'S':
                sx, sy = i, j
    
    visited = [[0] * m for i in range(n)]
    q = deque()
    q.append((sx, sy, 0))
    
    while q:
        x, y, step = q.popleft()
        if x == lx and y == ly:
            road1 = step
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                visited[nx][ny] = 1
                q.append((nx, ny, step + 1))
                
    visited = [[0] * m for i in range(n)]
    q = deque()
    q.append((lx, ly, 0))
    
    while q:
        x, y, step = q.popleft()
        if x == ex and y == ey:
            road2 = step
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                visited[nx][ny] = 1
                q.append((nx, ny, step + 1))
                
    if road1 == 0 or road2 == 0:
        return -1
    else:
        return road1 + road2