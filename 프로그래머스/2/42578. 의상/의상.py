from collections import defaultdict

def solution(clothes):
    answer = 1
    cloth_set = defaultdict(int)
    
    for cloth in clothes:
        cloth_set[cloth[1]] += 1
        
    for cs in cloth_set:
        answer *= cloth_set[cs] + 1
    
    return answer-1