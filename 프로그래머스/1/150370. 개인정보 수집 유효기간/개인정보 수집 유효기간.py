def solution(today, terms, privacies):
    answer = []
    valid = {}
    idx = 0
    
    year, month, day = date(today)
    
    for info in terms:
        a, b = info.split(' ')
        valid[a] = int(b)
    
    for info in privacies:
        a, b = info.split(' ')
        y, m, d = date(a)
        
        diff = (year - y) * 28 * 12 + (month - m) * 28 + (day - d)
        idx += 1
        
        print(diff, 28 * valid[b])
        if diff >= 28 * valid[b]:
            answer.append(idx)
    
    return answer

def date(today):
    year = int(today[0:4])
    month = int(today[5:7])
    day = int(today[8:10])
    
    return year, month, day