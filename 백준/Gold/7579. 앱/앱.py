import sys
input = sys.stdin.readline

n, target = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

answer = 10001

dp = [[0] * 10001 for _ in range(n+1)]
for i in range(1, n+1):
    m, c = memory[i-1], cost[i-1]
    for j in range(10001):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + m)

        if dp[i][j] >= target:
            answer = min(answer, j)

print(answer)