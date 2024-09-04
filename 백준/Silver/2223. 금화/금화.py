t, x, m = map(int, input().split())
answer = 0

if m == 0:
    answer = t * x
else:
    d, s = map(int, input().split())
    allowed = (d-1) // s
    
    for i in range(m-1):
        d, s = map(int, input().split())
        allowed = min(allowed, (d-1) // s)
        
    if allowed == 0:
        answer = 0
    elif allowed > t:
        answer = t * x
    else:
        answer = (allowed + (t - allowed) // 2) * x
        
print(answer)