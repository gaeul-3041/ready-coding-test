n, k = map(int, input().split())
dp = [[0] * (k + 1) for i in range(n + 1)]

bag = [[0, 0]]
ans = 0

for i in range(n):
    bag.append(list(map(int, input().split())))

for i in range(n + 1):
    w, v = bag[i][0], bag[i][1]
    for j in range(k + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])

print(dp[n][k])