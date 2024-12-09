def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    pboard = [[0] * (m + 1) for i in range(n + 1)]
    
    for t, x1, y1, x2, y2, d in skill:
        pattern = d * (-1)
        if t == 2:
            pattern *= -1
        pboard[x1][y1] += pattern
        pboard[x1][y2 + 1] -= pattern
        pboard[x2 + 1][y1] -= pattern
        pboard[x2 + 1][y2 + 1] += pattern
        
    for i in range(n):
        for j in range(1, m):
            pboard[i][j] += pboard[i][j - 1]
        
    for i in range(1, n):
        for j in range(m):
            pboard[i][j] += pboard[i - 1][j]
        
    for i in range(n):
        for j in range(m):
            board[i][j] += pboard[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer