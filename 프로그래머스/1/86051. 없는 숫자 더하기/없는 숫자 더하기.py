def solution(numbers):
    array = [x for x in range(10) if x not in numbers]
    
    return sum(array)