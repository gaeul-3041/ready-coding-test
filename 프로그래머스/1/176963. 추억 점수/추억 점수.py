def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for people in photo:
        tmp = 0
        for p in people:
            if p in dic.keys():
                tmp += dic[p]
        answer.append(tmp)
        
    return answer