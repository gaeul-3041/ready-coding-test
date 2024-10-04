import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def throw(k):
    x, y = 0, 0

    if turn == 1:
        for i in range(r):
            if cave[k][i] == 'x':
                cave[k][i] = '.'
                x, y = k, i
                break
    else:
        for i in range(r-1, -1, -1):
            if cave[k][i] == 'x':
                cave[k][i] = '.'
                x, y = k, i
                break
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and cave[nx][ny] == 'x':
            mineral_q.append((nx, ny))

def find(x, y):
    q = deque()
    visited = [[False] * c for _ in range(r)]

    q.append((x, y))
    visited[x][y] = True
    baseline = []

    while q:
        x, y = q.popleft()
        if x == r-1:
            return
        if cave[x+1][y] == '.':
            baseline.append((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and cave[nx][ny] == 'x' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

    move(baseline, visited)

def move(baseline, visited):
    down, chk = 0, False

    while True:
        down += 1
        for x, y in baseline:
            if x + down == r-1 or (cave[x][y] == 'x' and not visited[x][y]):
                chk = True
                break
        if chk:
            break

    for i in range(r-2, -1, -1):
        for j in range(c):
            if cave[i][j] == 'x' and visited[i][j]:
                cave[i][j] = '.'
                cave[i+down][j] = 'x'


r, c = map(int, input().split())
cave = [list(input()) for _ in range(r)]

n = int(input())
height = list(map(int, input().split()))

mineral_q = deque()
turn = 1

for h in height:
    throw(r-h)
    turn *= -1

    while mineral_q:
        x, y = mineral_q.popleft()
        find(x, y)

for i in range(r):
    for j in range(c):
        print(cave[i][j], end='')
    print()