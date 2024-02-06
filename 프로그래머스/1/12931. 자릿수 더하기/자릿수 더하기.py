def solution(n):
    array = [n for n in str(n)]
    answer = 0
    
    for i in array:
        answer += int(i)
    
    return answer

    