def solution(my_string):
    try:
        result = eval(my_string)
        return result
    except:
        return "수식이 올바르지 않습니다."