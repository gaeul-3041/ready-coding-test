def solution(commands):
    answer = []
    board = [['EMPTY'] * 51 for i in range(51)]
    merge = [[(i, j) for j in range(51)] for i in range(51)]
    
    for command in commands:
        command = list(command.split())
        order = command.pop(0)
        
        if order == 'UPDATE':
            if len(command) > 2:
                r, c, v = int(command[0]), int(command[1]), command[2]
                x, y = merge[r][c]
                board[x][y] = v
            else:
                v1, v2 = command[0], command[1]
                for i in range(1, 51):
                    for j in range(1, 51):
                        if board[i][j] == v1:
                            board[i][j] = v2
                            
        elif order == 'MERGE':
            r1, c1, r2, c2 = int(command[0]), int(command[1]), int(command[2]), int(command[3])
            
            if r1 == r2 and c1 == c2:
                continue
            
            x1, y1 = merge[r1][c1]
            x2, y2 = merge[r2][c2]
            v = ''
            
            if board[x1][y1] == 'EMPTY':
                v = board[x2][y2]
            else:
                v = board[x1][y1]
            
            for i in range(1, 51):
                for j in range(1, 51):
                    if merge[i][j] == (x2, y2):
                        merge[i][j] = (x1, y1)
                
            board[x1][y1] = v
                        
        elif order == 'UNMERGE':
            r, c = int(command[0]), int(command[1])
            x, y = merge[r][c]
            v = board[x][y]
            
            for i in range(1, 51):
                for j in range(1, 51):
                    if merge[i][j] == (x, y):
                        merge[i][j] = (i, j)
                        board[i][j] = 'EMPTY'
                        
            board[r][c] = v
            
        else:
            r, c = int(command[0]), int(command[1])
            x, y = merge[r][c]
            answer.append(board[x][y])
    
    return answer