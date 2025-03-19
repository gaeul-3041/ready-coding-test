import math

def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    finish = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    
    cnt = 0
    maxDate = finish[0]
    
    for i in range(n):
        if finish[i] <= maxDate:
            cnt += 1
        else:
            maxDate = finish[i]
            answer.append(cnt)
            cnt = 1
    
    answer.append(cnt)
    return answer