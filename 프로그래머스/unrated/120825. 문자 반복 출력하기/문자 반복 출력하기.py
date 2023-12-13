def solution(my_string, n):
    result = ''
    for char in my_string:
        result += char * n
    return result