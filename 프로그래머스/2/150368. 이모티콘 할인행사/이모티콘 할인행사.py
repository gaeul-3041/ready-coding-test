from itertools import product

def solution(users, emoticons):
    discount = [10, 20, 30, 40]
    answer = [0, 0]
    
    for sales in product(discount, repeat = len(emoticons)):
        res = [0, 0]
        for user in users:
            tmp = 0
            for i in range(len(emoticons)):
                if user[0] <= sales[i]:
                    tmp += emoticons[i] * (100 - sales[i]) / 100
            if tmp >= user[1]:
                res[0] += 1
            else:
                res[1] += tmp
                
        answer = max(answer, res)
    
    return answer