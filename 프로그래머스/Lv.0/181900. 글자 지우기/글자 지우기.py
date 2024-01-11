def solution(my_string, indices):
    result = ''.join(my_string[i] for i in range(len(my_string)) if i not in indices)
    return result