import heapq
import sys
input = sys.stdin.readline

n = int(input())
left = []
right = []

for i in range(n):
    k = int(input())
    
    if i == 0:
        heapq.heappush(left, -k)
        print(-left[0])
        continue
    
    if k <= -left[0]:
        heapq.heappush(left, -k)
    else:
        heapq.heappush(right, k)
        
    if len(left) > len(right) + 1:
        move = -heapq.heappop(left)
        heapq.heappush(right, move)
    elif len(right) > len(left):
        move = heapq.heappop(right)
        heapq.heappush(left, -move)
    
    print(-left[0])