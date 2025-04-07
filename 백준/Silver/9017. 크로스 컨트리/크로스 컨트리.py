from collections import defaultdict

tc = int(input())

for _ in range(tc):
    n = int(input())
    t = list(map(int, input().split()))

    members = defaultdict(int)
    verified = []

    for i in range(n):
        members[t[i]] += 1

    for k, v in members.items():
        if v == 6:
            verified.append(k)

    scores = defaultdict(list)
    rank = 1

    for i in range(n):
        if t[i] in verified:
            scores[t[i]].append(rank)
            rank += 1

    answer = sorted(scores, key=lambda x: (sum(scores[x][0:4]), scores[x][4]))[0]
    print(answer)