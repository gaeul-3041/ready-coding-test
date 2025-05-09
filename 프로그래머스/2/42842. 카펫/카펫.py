def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, int(total ** 0.5) + 1):
        if total % i != 0:
            continue
        j = total // i
        if (i - 2) * (j - 2) == yellow:
            return [j, i]