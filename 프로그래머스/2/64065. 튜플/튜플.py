from collections import defaultdict

def solution(s):
    answer = defaultdict(int)
    tup = sorted(s[2:-2].split('},{'), key=len)
    
    for t in tup:
        nums = t.split(',')
        for num in nums:
            n = int(num)
            answer[n] += 1

    return list(answer)