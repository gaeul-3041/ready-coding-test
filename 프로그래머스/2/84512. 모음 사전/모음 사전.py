alpha = ['A', 'E', 'I', 'O', 'U']
dictionary = []

def makeDic(s, length):
    if length > 5:
        return
    if s != '':
        dictionary.append(s)
    for a in alpha:
        makeDic(s+a, length + 1)

def solution(word):
    makeDic('', 0)
    for i in range(len(dictionary)):
        if dictionary[i] == word:
            return i + 1