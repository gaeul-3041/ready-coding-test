from collections import defaultdict

def solution(s):
    count = defaultdict(int)
    tup = s[2:-2].split('},{')
    
    for t in tup:
        nums = t.split(',')
        for num in nums:
            n = int(num)
            count[n] += 1
    
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    answer = []
    for c in count:
        answer.append(c[0])
    
    return answer