def solution(a, b):
    answer = 0
    
    # a가 b보다 작은 경우
    if a < b:
        for i in range(a, b + 1):
            answer += i
    # a가 b보다 큰 경우
    else:
        for i in range(b, a + 1):
            answer += i
    
    return answer

    