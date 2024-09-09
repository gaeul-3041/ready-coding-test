from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001

q = deque()
q.append((n, 0))

while q:
    m, step = q.popleft()
    visited[m] = 1
    if m == k:
        print(step)
        break

    idx = m + 1
    if 0 <= idx < 100001 and visited[idx] == 0:
        q.append((idx, step + 1))
        visited[idx] = 1

    idx = m - 1
    if 0 <= idx < 100001 and visited[idx] == 0:
        q.append((idx, step + 1))
        visited[idx] = 1

    idx = m * 2
    if 0 <= idx < 100001 and visited[idx] == 0:
        q.append((idx, step + 1))
        visited[idx] = 1