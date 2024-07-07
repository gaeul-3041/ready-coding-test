def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        tmp = 10000000
        
        d1 = (startX - x) ** 2 + (startY - 2 * n + y) ** 2
        d2 = (startX - 2 * m + x) ** 2 + (startY - y) ** 2
        d3 = (startX - x) ** 2 + (startY + y) ** 2
        d4 = (startX + x) ** 2 + (startY - y) ** 2
        
        if startY == y and startX > x:
            tmp = min(tmp, d1, d2, d3)
        elif startY == y and startX < x:
            tmp = min(tmp, d1, d3, d4)
        elif startX == x and startY > y:
            tmp = min(tmp, d1, d2, d4)
        elif startX == x and startY < y:
            tmp = min(tmp, d2, d3, d4)
        else:
            tmp = min(tmp, d1, d2, d3, d4)
            
        answer.append(tmp)
    
    return answer