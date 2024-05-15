import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []

for i in range(n):
    a.append(int(input()))

a.sort()
dic = {}

for i in range(n):
    if a[i] not in dic:
        dic[a[i]] = i
    
for i in range(m):
    question = int(input())
    if question in dic:
        print(dic[question])
    else:
        print(-1)