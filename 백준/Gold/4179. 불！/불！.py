from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q_fire:
        x, y = q_fire.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] != '#' and visited_fire[nx][ny] == 0:
                visited_fire[nx][ny] = visited_fire[x][y] + 1
                q_fire.append((nx, ny))
    
    while q_human:
        x, y = q_human.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if maze[nx][ny] != '#' and visited_human[nx][ny] == 0 and (visited_fire[nx][ny] == 0 or visited_fire[nx][ny] > visited_human[x][y] + 1):
                    visited_human[nx][ny] = visited_human[x][y] + 1
                    q_human.append((nx, ny))
            else:
                return visited_human[x][y]
    
    return 'IMPOSSIBLE'


r, c = map(int, input().split())
maze = []

q_fire = deque()
q_human = deque()

visited_fire = [[0] * c for _ in range(r)]
visited_human = [[0] * c for _ in range(r)]

for i in range(r):
    row = list(input())
    maze.append(row)
    
    for j in range(c):
        if row[j] == 'J':
            q_human.append((i, j))
            visited_human[i][j] = 1
        elif row[j] == 'F':
            q_fire.append((i, j))
            visited_fire[i][j] = 1
            
print(bfs())