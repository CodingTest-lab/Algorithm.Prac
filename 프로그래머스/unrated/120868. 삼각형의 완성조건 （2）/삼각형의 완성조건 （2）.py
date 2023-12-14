def solution(sides):
    count = 0
    for x in range (sum(sides)):
        if x + min(sides) > max(sides) and sum(sides) > x:
            count += 1

    return count
            