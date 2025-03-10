h, w = map(int, input().split())
blocks = list(map(int, input().split()))

answer = 0

for i in range(1, w-1):
    left = max(blocks[:i])
    right = max(blocks[i+1:])
    min_h = min(left, right)
    
    if blocks[i] < min_h:
        answer += min_h - blocks[i]

print(answer)