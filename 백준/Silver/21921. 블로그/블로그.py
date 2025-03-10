n, x = map(int, input().split())
visiters = list(map(int, input().split()))

if max(visiters) == 0:
    print('SAD')
else:
    answer = sum(visiters[:x])
    visit = answer
    cnt = 1

    for i in range(n-x):
        visit += visiters[i+x]
        visit -= visiters[i]
    
        if visit > answer:
            answer = visit
            cnt = 1
        elif visit == answer:
            cnt += 1
       
    print(answer)
    print(cnt)