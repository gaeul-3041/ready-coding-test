def factorial(n):
    cnt = 1
    for i in range(2, n+1):
        cnt = (cnt * i) % p
    return cnt

def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    
    m = square(n, k // 2)
    if k % 2 == 0:
        return (m * m) % p
    else:
        return (m * m * n) % p

n, k = map(int, input().split())
p = 1000000007

a = factorial(n) % p
b = factorial(k) * factorial(n-k) % p

print(a * square(b, p-2) % p)