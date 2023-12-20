def solution(n):
    i = 1
    x = 1

    while x <= n:
        i += 1
        x *= i

    return i - 1