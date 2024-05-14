def solution(bandage, health, attacks):
    final = attacks[-1][0]
    t, x, y = bandage
    maxHealth = health
    con = 0
    
    for i in range(1, final + 1):
        d = 0
        attacked = 0
        print(health)
        if con == t:
            health = min(health + y, maxHealth)
            con = 0
        for j in range(len(attacks)):
            if i == attacks[j][0]:
                attacked = 1
                d = attacks[j][1]
                break
        if attacked == 1:
            health -= d
            con = 0
        else:
            health = min(health + x, maxHealth)
            con += 1
        if health <= 0:
            return -1
        
    return health