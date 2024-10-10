n = int(input())
k = 1000000
p = (15 * k) // 10

dp = [0] * p
dp[1] = 1

for i in range(2, p):
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= k
    
print(dp[n % p])