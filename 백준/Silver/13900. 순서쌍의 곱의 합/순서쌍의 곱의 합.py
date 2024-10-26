n = int(input())
numbers = list(map(int, input().split()))
answer = 0
s = sum(numbers)

for i in range(n-1):
    s -= numbers[i]
    answer += s * numbers[i] 

print(answer)