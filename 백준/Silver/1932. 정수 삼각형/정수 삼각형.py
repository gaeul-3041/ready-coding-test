n = int(input())
tree = []

for i in range(n):
    tree.append(list(map(int, input().split())))
    
dp = [[0] * n for _ in range(n)]
dp[0][0] = tree[0][0]

for i in range(1, n):
    for j in range(len(tree[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tree[i][j]
        elif j == len(tree[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + tree[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tree[i][j]

print(max(dp[n-1]))