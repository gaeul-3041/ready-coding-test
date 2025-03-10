s = input()
key = input()
stack = []

for i in s:
    stack.append(i)
    if ''.join(stack[-len(key):]) == key:
        for j in range(len(key)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')