from itertools import combinations, product

def solution(dice):    
    n = len(dice)
    scoreBoard = {}
    
    for diceA in combinations(range(n), n//2):
        scoreA, scoreB = [], []
        
        diceB = [i for i in range(n) if i not in diceA]
        
        for p in product(range(6), repeat=n//2):
            scoreA.append(sum(dice[i][j] for i, j in zip(diceA, p)))
            scoreB.append(sum(dice[i][j] for i, j in zip(diceB, p)))
        
        scoreB.sort()
        
        w = 0
        
        for score in scoreA:
            left, right = 0, len(scoreB) - 1
            while left <= right:
                mid = (left + right) // 2
                if score <= scoreB[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            w += left
        
        scoreBoard[diceA] = w
    
    answer = max(scoreBoard, key=scoreBoard.get)
    return [i+1 for i in answer]