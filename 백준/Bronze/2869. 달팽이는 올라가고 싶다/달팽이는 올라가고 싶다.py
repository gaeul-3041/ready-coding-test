import math

a, b, v = map(int, input().split())
climb = 0
day = math.ceil((v-b)/(a-b))

print(day)