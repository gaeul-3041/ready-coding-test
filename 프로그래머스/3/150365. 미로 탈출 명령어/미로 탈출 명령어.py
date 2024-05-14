import sys
sys.setrecursionlimit(10**8)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
direction = ['d', 'l', 'r', 'u']
answer = 'z'

def dfs(n, m, x, y, r, c, k, parent, step):
    global answer
    if k < step + abs(x - r) + abs(y - c):
        return
    if x == r and y == c and step == k:
        answer = parent
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        child = parent + direction[i]
        if 1 <= nx <= n and 1 <= ny <= m and parent < answer:
            dfs(n, m, nx, ny, r, c, k, child, step + 1)

def solution(n, m, x, y, r, c, k):
    d = abs(x - r) + abs(y - c)
    if (d - k) % 2 == 1 or d > k:
        return 'impossible'
    
    dfs(n, m, x, y, r, c, k, '', 0)
    return answer