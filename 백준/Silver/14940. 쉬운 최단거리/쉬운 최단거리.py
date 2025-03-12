from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

start_x, start_y = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i, j
            break

q = deque()
q.append((start_x, start_y))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1
        print(visited[i][j], end=' ')
    print()