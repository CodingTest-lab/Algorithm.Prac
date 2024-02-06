def solution(n):
    array1 = [x for x in range (1,n+1)]
    answer = []
    
    for i in array1:
        
        if n % i == 1:
            answer.append(i)
    
    return min(answer)