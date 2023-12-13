def solution(n):
    count = 0
    for i in range (1,n+1):
        if n % i == 0:
            count += 1
    return count

#0으로 나누면 안된다... 
        