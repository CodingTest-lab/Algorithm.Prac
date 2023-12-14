def solution(rsp):
    result = ''
    for i in range(len(rsp)):
        if rsp[i] == '2':
            result += '0'
        elif rsp[i] == '5':
            result += '2'
        elif rsp[i] == '0':
            result += '5'
        
    return result
