from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 0
answer = 0

numbers = defaultdict(int)

while right < n:
    if numbers[a[right]] < k:
        numbers[a[right]] += 1
        right += 1
    else:
        numbers[a[left]] -= 1
        left += 1
    answer = max(answer, right - left)
    
print(answer)