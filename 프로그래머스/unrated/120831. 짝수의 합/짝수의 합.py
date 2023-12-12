def solution(n):
    count = 0
    for i in range(n+1):
        if i % 2 == 0:
            count += i
    return count
