def solution(n):
    result = set()
    div = 2

    while n > 1:
        if n % div == 0:
            result.add(div)
            n //= div
        else:
            div += 1

    return sorted(result) 

