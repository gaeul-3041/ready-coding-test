def dfs(x, y, power):
    global answer
    if y == m:
        x, y = x+1, 0
    if x == n:
        answer = max(answer, power)
        return
    for i in range(4):
        nx1, ny1 = x + dx[i], y + dy[i]
        nx2, ny2 = x + dx[i-1], y + dy[i-1]
        if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m and not visited[x][y] and not visited[nx1][ny1] and not visited[nx2][ny2]:
            visited[x][y] = visited[nx1][ny1] = visited[nx2][ny2] = True
            dfs(x, y + 1, power + 2 * board[x][y] + board[nx1][ny1] + board[nx2][ny2])
            visited[x][y] = visited[nx1][ny1] = visited[nx2][ny2] = False
   
    dfs(x, y + 1, power)
                
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dfs(0, 0, 0)
print(answer)