def solution(x, n):
    array1 = [i for i in range(1, n + 1)]
    answer = []
    
    for i in array1:
        answer.append(x * i)
    
    return answer