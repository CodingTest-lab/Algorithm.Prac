def solution(before, after):
    result_before = sorted(before)
    result_after = sorted(after)
    if result_before == result_after:
        return 1
    else:
        return 0