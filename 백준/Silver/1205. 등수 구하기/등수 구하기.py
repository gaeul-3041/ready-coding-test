n, score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    rank = list(map(int, input().split()))
    rank.append(score)
    rank.sort(reverse=True)

    answer = -1

    idx = rank.index(score)
    if idx + rank.count(score) <= p:
        answer = idx + 1

    print(answer)