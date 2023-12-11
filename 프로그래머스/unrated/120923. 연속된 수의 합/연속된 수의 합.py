def solution(num, total):
    answer = []
    
    start_value = total // num - (num - 1) // 2
    
    # num개의 연속된 수를 더한 값이 total이 되도록 배열 생성
    for i in range(num):
        answer.append(start_value + i)
    
    return answer
