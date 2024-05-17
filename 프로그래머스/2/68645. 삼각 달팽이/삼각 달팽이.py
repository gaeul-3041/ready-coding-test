def solution(n):
    answer = []
    board = [[0] * n for i in range(n)]
    x, y, cnt = -1, 0, 0
    num = 1
    
    for i in range(n, 0, -1):
        if cnt % 3 == 0:
            for j in range(i):
                x += 1
                board[x][y] = num
                num += 1
                
        elif cnt % 3 == 1:
            for j in range(i):
                y += 1
                board[x][y] = num
                num += 1
        
        else:
            for j in range(i):
                x -= 1
                y -= 1
                board[x][y] = num
                num += 1
                
        cnt += 1
        
    for i in range(n):
        for j in range(i + 1):
            answer.append(board[i][j])
                
    return answer