r, g, b = map(int, input().split())
answer = r // 3 + g // 3 + b // 3

lefts = [r % 3, g % 3, b % 3]
cnt = 0
for i in range(3):
    if lefts[i] > 0:
        cnt += 1
        
if cnt == 1:
    answer += 1
else:
    answer += max(lefts)

print(answer)