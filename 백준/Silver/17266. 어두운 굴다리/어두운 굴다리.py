def check_light(k):
    if light[0] > k:
        return False
    for i in range(1, m):
        if light[i] - light[i-1] > k * 2:
            return False
    if light[-1] + k < n:
        return False
    
    return True

n = int(input())
m = int(input())
light = list(map(int, input().split()))

start, end, answer = 1, n, 0

while start <= end:
    mid = (start + end) // 2
    
    if check_light(mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
        
print(answer)