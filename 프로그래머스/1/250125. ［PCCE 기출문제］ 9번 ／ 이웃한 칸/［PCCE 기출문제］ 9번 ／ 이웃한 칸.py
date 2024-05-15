def solution(board, h, w):
    answer = 0
    
    n = len(board)
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]
    
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if 0 <= nh < n and 0 <= nw < n:
            if board[nh][nw] == board[h][w]:
                answer += 1
    
    return answer