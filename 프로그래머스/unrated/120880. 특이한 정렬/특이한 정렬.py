def solution(numlist, n):
    # numlist의 각 원소에 대한 거리 및 크기를 기준으로 정렬
    numlist.sort(key=lambda x: (abs(x - n), -x))
    return numlist