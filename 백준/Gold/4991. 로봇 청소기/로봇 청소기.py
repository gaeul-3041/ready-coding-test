from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited = [[0] * w for _ in range(h)]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0  and room[nx][ny] != 'x':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    
    return visited


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    room = [list(input()) for _ in range(h)]
    dirty = []
    answer = -1
    sx, sy = 0, 0

    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o':
                sx, sy = i, j
            elif room[i][j] == '*':
                dirty.append((i, j))

    n = len(dirty)
    first_distance = [0] * n
    distance = [[0] * n for _ in range(n)]

    visited = bfs(sx, sy)
    chk = 1

    for i in range(n):
        dtx, dty = dirty[i][0], dirty[i][1]
        if visited[dtx][dty] == 0:
            chk = 0
            break
        first_distance[i] = visited[dtx][dty] - 1
    
    if chk == 1:
        answer = 10 ** 9
        
        for i in range(n-1):
            ix, iy = dirty[i][0], dirty[i][1]
            visited = bfs(ix, iy)
            for j in range(i+1, n):
                jx, jy = dirty[j][0], dirty[j][1]
                distance[i][j] = distance[j][i] = visited[jx][jy] - 1

        for per in permutations(range(len(distance))):
            cur = per[0]
            steps = first_distance[cur]
            for i in range(1, len(per)):
                nxt = per[i]
                steps += distance[cur][nxt]
                cur = nxt
            answer = min(answer, steps)

    print(answer)