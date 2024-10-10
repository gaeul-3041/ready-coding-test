from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[-1] * (w+2) for _ in range(h+2)]
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h+2 and 0 <= ny < w+2 and visited[nx][ny] == -1 and maze[nx][ny] != '*':
                if maze[nx][ny] == '#':
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                else:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
    
    return visited


tc = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(tc):
    h, w = map(int, input().split())
    maze = []
    answer = h * w

    maze.append(list('.' * (w+2)))
    for i in range(h):
        maze.append(list('.'+input()+'.'))
    maze.append(list('.' * (w+2)))

    prisoner = []
    for i in range(h+2):
        for j in range(w+2):
            if maze[i][j] == '$':
                prisoner.append((i, j))
                maze[i][j] = '.'
    
    p1 = bfs(prisoner[0][0], prisoner[0][1])
    p2 = bfs(prisoner[1][0], prisoner[1][1])
    p0 = bfs(0, 0)

    for i in range(h+2):
        for j in range(w+2):
            if p1[i][j] > -1 and p2[i][j] > -1 and p0[i][j] > -1 and maze[i][j] != '*':
                cnt = p1[i][j] + p2[i][j] + p0[i][j]
                if maze[i][j] == '#':
                    cnt -= 2
                answer = min(answer, cnt)

    print(answer)