tc = int(input())

for t in range(tc):
    n = int(input())
    p = list(map(int, input().split()))
    discount = []
    
    for i in range(n*2):
        if p[i] == 0:
            continue
        for j in range(i+1, n*2):
            if p[i] == p[j] * 0.75:
                discount.append(p[i])
                p[i] = 0
                p[j] = 0
                break
                
    
    print(f'Case #{t+1}:', end=' ')
    for answer in discount:
        print(answer, end=' ')