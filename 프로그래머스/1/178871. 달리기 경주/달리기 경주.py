def solution(players, callings):
    pr = {}
    rp = {}
    
    for i in range(len(players)):
        rp[i + 1] = players[i]
        pr[players[i]] = i + 1
        
    for calling_player in callings:
        calling_rank = pr[calling_player]
        above_rank = calling_rank - 1
        above_player = rp[above_rank]
        
        pr[calling_player] -= 1
        pr[above_player] += 1
        rp[calling_rank] = above_player
        rp[above_rank] = calling_player
    
    return list(rp.values())