def solution(my_string):
    your_string = my_string.upper()
    result = ''
    for i in range (len(my_string)):
        if your_string[i] != my_string[i]:
            result += your_string[i]
        elif your_string[i] == my_string[i]:
            result += your_string[i].lower()
    return result