from collections import deque

def solution(enroll, referral, seller, amount):
    answer = []
    link = {}
    
    for i, j in zip(enroll, referral):
        link[i] = [j, 0]
        
    for a, b in zip(seller, amount):
        q = deque()
        q.append((a, b * 100))
        while q:
            sell, cost = q.popleft()
            if sell == '-':
                break
            tmp = cost // 10
            if tmp == 0:
                link[sell][1] += cost
            else:
                link[sell][1] += cost - tmp
                q.append((link[sell][0], tmp))
                
    for v in link.values():
        answer.append(v[1])
    
    return answer