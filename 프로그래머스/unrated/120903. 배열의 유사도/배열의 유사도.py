def solution(s1, s2):
    common_elements = set(s1) & set(s2)
    return len(common_elements)


