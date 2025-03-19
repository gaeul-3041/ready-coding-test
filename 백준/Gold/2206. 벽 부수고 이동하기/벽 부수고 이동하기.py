from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mat = []
visited = [[[0] * 2 for i in range(m)] for j in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    mat.append(list(input()))

def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][z] == 0:
                if mat[nx][ny] == '0':
                    q.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
                if mat[nx][ny] == '1' and z == 0:
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][z] + 1
    return -1

print(bfs())