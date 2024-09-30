def matrix_decompose(a, b):
    if b == 1:
        return a
    m = matrix_decompose(a, b // 2)
    if b % 2 == 0:
        return matrix_multiple(m, m)
    else:
        return matrix_multiple(matrix_multiple(m, m), a)
    
def matrix_multiple(m1, m2):
    m3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                m3[i][j] += (m1[i][k] * m2[k][j]) % 1000
    return m3


n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

answer = matrix_decompose(a, b)
for i in range(n):
    for j in range(n):
        print(answer[i][j] % 1000, end=' ')
    print()