def solution(my_string):
    result = my_string.lower()
    t_result = ''.join(sorted(result))
    return t_result