def solution(plans):
    answer = []
    process = []
    
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key = lambda x : x[1])
    
    for i in range(len(plans) - 1):
        name, start, playtime = plans[i]
        next_name, next_start, next_playtime = plans[i+1]
        
        if start + playtime <= next_start:
            answer.append(name)
            left_time = next_start - (start + playtime)
            
            while left_time > 0 and process:
                n, s, p = process.pop()
                if left_time >= p:
                    answer.append(n)
                    left_time -= p
                else:
                    process.append([n, s, p - left_time])
                    left_time = 0
                    
        else:
            playtime -= (next_start - start)
            process.append([name, start, playtime])
            
    answer.append(plans[-1][0])
    
    while process:
        n = process.pop()[0]
        answer.append(n)
    
    return answer