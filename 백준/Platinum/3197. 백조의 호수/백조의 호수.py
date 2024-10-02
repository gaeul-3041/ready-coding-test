import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_swan():
    while swan_q:
        x, y = swan_q.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not swan_visited[nx][ny]:
                swan_visited[nx][ny] = True
                if lake[nx][ny] == 'X':
                    swan_next_q.append((nx, ny))
                else:
                    swan_q.append((nx, ny))

    return False


r, c = map(int, input().split())
lake = [list(input()) for _ in range(r)]
swan = []
answer = 0

swan_visited = [[False] * c for _ in range(r)]

swan_q = deque()
lake_q = deque()
swan_next_q = deque()
lake_next_q = deque()

for i in range(r):
    for j in range(c):
        if lake[i][j] == 'L':
            swan.append((i, j))
            lake_q.append((i, j))
            lake[i][j] = '.'
        elif lake[i][j] == '.':
            lake_q.append((i, j))

sx, sy = swan[0]
ex, ey = swan[1]
swan_q.append((sx, sy))
swan_visited[sx][sy] = True

while True:
    if bfs_swan():
        print(answer)
        break

    answer += 1
    while lake_q:
        x, y = lake_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and lake[nx][ny] == 'X':
                lake_next_q.append((nx, ny))
                lake[nx][ny] = '.'
    
    swan_q, lake_q = swan_next_q, lake_next_q
    swan_next_q, lake_next_q = deque(), deque()