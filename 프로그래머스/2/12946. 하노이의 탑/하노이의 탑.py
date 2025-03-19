answer = []

def hanoi(start, via, end, n):
    if n == 1:
        answer.append([start, end])
        return
    hanoi(start, end, via, n-1)
    answer.append([start, end])
    hanoi(via, start, end, n-1)

def solution(n):
    hanoi(1, 2, 3, n)
    return answer