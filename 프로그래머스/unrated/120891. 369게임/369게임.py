def solution(order):
    count = 0
    s_order = str(order)
    for i in range (len(s_order)):
        if s_order[i] == '3':
            count += 1 
        elif s_order[i] == '6':
            count += 1   
        elif s_order[i] == '9':
            count += 1
    return count 

#len()함수는 int에 적용이 안됨 / str로 바꿨기때문에 int랑 비교가 아닌 string의 값으로 비교 해야됨.... 
        