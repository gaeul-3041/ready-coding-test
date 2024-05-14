def solution(friends, gifts):
    k = len(friends)
    answer = [0 for i in range(k)]
    giftidx = [0 for i in range(k)]
    numbers = {}
    giftlog = [[0] * k for i in range(k)]
    
    for i in range(k):
        numbers[friends[i]] = i
        
    for gift in gifts:
        src, dst = gift.split(' ')
        giftlog[numbers[src]][numbers[dst]] += 1
        giftidx[numbers[src]] += 1
        giftidx[numbers[dst]] -= 1
        
    for i in range(k):
        for j in range(i+1, k):
            if giftlog[i][j] > giftlog[j][i]:
                answer[i] += 1
            elif giftlog[i][j] < giftlog[j][i]:
                answer[j] += 1
            else:
                if giftidx[i] > giftidx[j]:
                    answer[i] += 1
                elif giftidx[i] < giftidx[j]:
                    answer[j] += 1
        
    return max(answer)