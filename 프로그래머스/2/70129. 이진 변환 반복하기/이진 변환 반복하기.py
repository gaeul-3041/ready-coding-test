def solution(s):
    cnt = 0
    removed = 0
    
    while s != '1':
        cnt += 1
        s1 = len(s)
        s2 = s.count('1')
        removed += s1 - s2
        s = bin(s2)[2:]
    
    return [cnt, removed]