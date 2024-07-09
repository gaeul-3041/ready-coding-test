import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
answer = 0
hq = []

jewels = []
bags = [0 for i in range(k)]

for i in range(n):
    m, v = map(int, input().split())
    jewels.append([m, v])
    
for i in range(k):
    bags[i] = int(input())
    
jewels.sort()
bags.sort()

for bag in bags:
    while jewels:
        m, v = jewels[0][0], jewels[0][1]
        if m <= bag:
            heapq.heappush(hq, -v)
            heapq.heappop(jewels)
        else:
            break
    if hq:
        answer -= heapq.heappop(hq)
        
print(answer)