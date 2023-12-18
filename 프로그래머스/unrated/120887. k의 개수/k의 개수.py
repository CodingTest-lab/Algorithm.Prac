def solution(i, j, k):
    count = 0
    for x in range(i, j + 1):
        if x < 10 and k == x:
            count += 1
        elif x >= 10:
            t = str(x)
            for m in range(len(t)):
                if k == int(t[m]):
                    count += 1
    return count


