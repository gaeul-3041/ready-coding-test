n, k = map(int, input().split())
line = list(input())

answer = 0

for i in range(n):
    if line[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0 <= j < n and line[j] == 'H':
                answer += 1
                line[j] = 'X'
                break

print(answer)