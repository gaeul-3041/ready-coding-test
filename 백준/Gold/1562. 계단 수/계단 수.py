n = int(input())
mod = 1000000000

answer = [[0] * 1024 for _ in range(10)]

for i in range(1, 10):
    answer[i][1<<i] = 1
    
for i in range(1, n):
    dp = [[0] * 1024 for _ in range(10)]
    for j in range(10):
        for k in range(1024):
            if j > 0:
                dp[j][k|(1<<j)] = (dp[j][k|(1<<j)] + answer[j-1][k]) % mod
            if j < 9:
                dp[j][k|(1<<j)] = (dp[j][k|(1<<j)] + answer[j+1][k]) % mod
    answer = dp

print(sum(answer[i][1023] for i in range(10)) % mod)