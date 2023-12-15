def solution(my_string):
    

    unique_chars = "".join(sorted(set(my_string), key=my_string.index))

    return unique_chars
