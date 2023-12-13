def solution(n):
    count = []
    for i in range (1,n+1):
        if i % 2 != 0:
             count.append(i)
    return count 