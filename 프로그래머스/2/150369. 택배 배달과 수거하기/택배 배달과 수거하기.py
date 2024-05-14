def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliveries.reverse()
    pickups.reverse()
    
    a = 0
    b = 0
    
    for i in range(n):
        a += deliveries[i]
        b += pickups[i]
        
        while a > 0 or b > 0:
            a -= cap
            b -= cap
            answer += (n - i) * 2
    
    return answer