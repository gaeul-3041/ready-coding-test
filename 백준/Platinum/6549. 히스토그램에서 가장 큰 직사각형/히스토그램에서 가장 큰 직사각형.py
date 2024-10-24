import sys
input = sys.stdin.readline

while True:
    heights = list(map(int, input().split())) + [0]
    if heights[0] == 0:
        break
    
    n = heights[0]
    stack = []
    answer = 0

    for i in range(1, n+1):
        height = heights[i]
        while stack and stack[-1][1] > height:
            s_i, s_height = stack.pop()
            start = 1
            if stack:
                start = stack[-1][0] + 1
            
            result = (i - start) * s_height
            answer = max(answer, result)

        stack.append((i, height))

    while stack:
        s_i, s_height = stack.pop()
        start = 1
        if stack:
            start = stack[-1][0] + 1

        result = (n + 1 - start) * s_height
        answer = max(answer, result)

    print(answer)