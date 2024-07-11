from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001

answer = 0
visited[n] = 1

q = deque()
q.append(n)

while q:
    cur = q.popleft()
    if cur == k:
        answer = visited[cur]
        break
    if 0 <= cur * 2 < 100001 and visited[cur * 2] == 0:
        q.appendleft(cur * 2)
        visited[cur * 2] = visited[cur]
    if 0 <= cur - 1 < 100001 and visited[cur - 1] == 0:
        q.append(cur - 1)
        visited[cur - 1] = visited[cur] + 1
    if 0 <= cur + 1 < 100001 and visited[cur + 1] == 0:
        q.append(cur + 1)
        visited[cur + 1] = visited[cur] + 1
        
print(answer - 1)