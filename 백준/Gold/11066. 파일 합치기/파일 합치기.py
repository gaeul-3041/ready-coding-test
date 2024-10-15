import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    k = int(input())
    files = [0] + list(map(int, input().split()))

    dp = [[0] * (k+1) for i in range(k+1)]

    for i in range(k+1):
        for j in range(k+1):
            if j == i+1:
                dp[i][j] = files[i] + files[j]

    for i in range(k-1, 0, -1):
        for j in range(1, k+1):
            if dp[i][j] == 0 and j > i:
                dp[i][j] = min(dp[i][k] + dp[k+1][j] for k in range(i, j)) + sum(files[i:j+1])

    print(dp[1][k])