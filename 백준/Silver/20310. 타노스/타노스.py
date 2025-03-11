s = list(input())
a, b = s.count('1'), s.count('0')

for i in range(a//2):
    s.pop(s.index('1'))
    
s = s[::-1]

for i in range(b//2):
    s.pop(s.index('0'))

s = s[::-1]
    
print(''.join(s))