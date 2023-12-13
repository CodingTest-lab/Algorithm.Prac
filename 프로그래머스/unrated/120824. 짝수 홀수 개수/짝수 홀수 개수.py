def solution(num_list):
    jak_su = 0
    hol_su = 0
    result = []
    
    for i in num_list:
        if i % 2 == 0:
            jak_su += 1
        else:
            hol_su += 1
    
    # append 함수를 사용하여 jak_su와 hol_su를 result 리스트에 추가
    result.append(jak_su)
    result.append(hol_su)
    
    return result
