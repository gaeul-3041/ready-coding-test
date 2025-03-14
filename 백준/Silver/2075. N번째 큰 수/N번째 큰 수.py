import heapq

n = int(input())
q = []

first_numbers = list(map(int, input().split()))
for i in range(n):
    heapq.heappush(q, first_numbers[i])

for i in range(n-1):
    numbers = list(map(int, input().split()))
    for j in range(n):
        if q[0] < numbers[j]:
            heapq.heappush(q, numbers[j])
            heapq.heappop(q)
            
print(q[0])