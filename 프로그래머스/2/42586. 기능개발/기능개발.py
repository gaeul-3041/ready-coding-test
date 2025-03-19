import math

def solution(progresses, speeds):
    answer = []
    
    for progress, speed in zip(progresses, speeds):
        days = math.ceil((100 - progress) / speed)
        if not answer or answer[-1][0] < days:
            answer.append([days, 1])
        else:
            answer[-1][1] += 1

    return [ans[1] for ans in answer]