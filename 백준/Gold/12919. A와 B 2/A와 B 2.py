def dfs(s, t):
    global answer
    if len(s) == len(t):
        if s == t:
            answer = 1
        return
    if t[-1] == 'A':
        dfs(s, t[:-1])
    if t[0] == 'B':
        dfs(s, t[1:][::-1])
    

s = list(input())
t = list(input())

answer = 0

dfs(s, t)
print(answer)