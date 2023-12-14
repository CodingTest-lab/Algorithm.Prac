def solution(array):
    max_value = max(array)
    #max_index 구하는 건 필수로 알아야겟다
    max_index = array.index(max_value)
    result = [max_value, max_index]
    return result
