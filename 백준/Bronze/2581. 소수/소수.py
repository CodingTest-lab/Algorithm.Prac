def solution(M, N):
    f = set(range(2, N + 1))
    t = set(range(M, N + 1))

    for i in range(2, int(N**0.5) + 1):
        if i in f:
            f -= set(range(2 * i, N + 1, i))

    result = f & t

    if sum(result) != 0:
        return sum(result), min(result)
    else:
        return -1, None

# 입력을 받고 결과를 출력하는 부분
M = int(input())
N = int(input())
sum_result, min_result = solution(M, N)
print(sum_result) if sum_result != -1 else print(-1)
print(min_result) if min_result else None
