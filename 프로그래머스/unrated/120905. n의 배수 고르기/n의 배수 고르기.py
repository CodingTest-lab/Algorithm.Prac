def solution(n, numlist):
    result = []
    for x in numlist:
        if x % n == 0:
            result.append(x)
    return result