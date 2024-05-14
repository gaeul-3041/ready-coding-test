import math

def solution(numbers):
    answer = []
    
    def search(word, midtree):
        if len(word) == 1:
            return True
        
        mid = len(word) // 2
        left = mid // 2
        right = mid * 2 - left
        
        if midtree == '0':
            if word[left] == '1' or word[right] == '1':
                return False
        
        return search(word[0:mid], word[left]) and search(word[mid+1:], word[right])
        
    
    for i in range(len(numbers)):
        n = numbers[i]
        nbin = bin(n)[2:]
        k = int(math.log2(len(nbin)) + 1)
        level = 2 ** k - 1
        ntree = '0' * (level - len(nbin)) + nbin
        
        mid = len(ntree) // 2
        
        if search(ntree, ntree[mid]):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer