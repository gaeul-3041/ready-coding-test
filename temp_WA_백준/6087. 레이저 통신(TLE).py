## 시간 초과
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

w, h = map(int, input().split())
board = [list(input()) for _ in range(h)]

c = []
for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            c.append((i, j))
            board[i][j] = '.'

sx, sy = c[0]
ex, ey = c[1]
visited = [[float('inf')] * w for _ in range(h)]

q = deque()
q.append((sx, sy))
visited[sx][sy] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        while True:
            if not (0 <= nx < h and 0 <= ny < w) or board[nx][ny] == '*' or visited[nx][ny] < visited[x][y] + 1:
                break
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            nx, ny = nx + dx[i], ny + dy[i]

print(visited[ex][ey] - 1)
