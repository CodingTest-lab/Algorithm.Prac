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
        