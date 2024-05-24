n = int(input())
ls = []
now = 0
ans = 0

for i in range(n):
    a, b = map(int, input().split())
    ls.append([a, b])
    
ls.sort(key = lambda ls: ls[0])
ls.sort(key = lambda ls: ls[1])

for i, j in ls:
    if i >= now:
        ans += 1
        now = j
        
print(ans)