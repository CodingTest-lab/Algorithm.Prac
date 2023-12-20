def solution(num_list, n):
    answer = []
    for i in range (len((num_list)) // n):
        if i == 0:
            answer.append(num_list[i:n])
        elif i != 0:
            answer.append(num_list[(i*n):((i*n)+n)])
        
    return answer