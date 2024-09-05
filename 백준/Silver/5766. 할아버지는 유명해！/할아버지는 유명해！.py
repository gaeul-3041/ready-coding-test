from collections import defaultdict

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    score = defaultdict(int)
    for i in range(n):
        ranking = list(map(int, input().split()))
        for r in ranking:
            score[r] += 1
            
    sorted_score = sorted(score.items(), key=lambda x : (-x[1], x[0]))
    second = sorted_score[1][1]
    
    for s in sorted_score:
        if s[1] == second:
            print(s[0], end=' ')
    print()