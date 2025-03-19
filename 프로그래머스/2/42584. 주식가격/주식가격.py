def solution(prices):
    date = len(prices)
    answer = [0] * date
    stack = [0]
    
    for i in range(1, date):
        while stack:
            if prices[i] < prices[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j
            else:
                break
        stack.append(i)
        
    while stack:
        j = stack.pop()
        answer[j] = date - 1 - j
    
    return answer