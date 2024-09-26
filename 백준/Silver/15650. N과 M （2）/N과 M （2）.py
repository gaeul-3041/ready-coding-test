from itertools import combinations

n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]

for com in combinations(numbers, m):
    for i in range(m):
        print(com[i], end=' ')
    print()