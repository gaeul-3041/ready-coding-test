from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []

def bfs(r, c, board):
    q = deque()
    q.append((r, c, 0))
    visited = [[0] * 5 for i in range(5)]
    visited[r][c] = 1
    
    while q:
        x, y, cnt = q.popleft()
        if board[x][y] == 'P' and cnt > 0:
            return False
        if cnt > 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0 and board[nx][ny] != 'X' and cnt < 2:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = 1
                    
    return True

def solution(places):
    for place in places:
        board = []
        for i in range(5):
            board.append(list(place[i]))
            
        ans = True
        for i in range(5):
            for j in range(5):
                if board[i][j] == 'P':
                    ans = ans & bfs(i, j, board)
                    print(ans)
        
        if ans:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer