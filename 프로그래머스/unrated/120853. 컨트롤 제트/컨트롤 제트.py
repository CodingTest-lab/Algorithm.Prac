def solution(s):
    tokens = s.split()  # 숫자와 "Z"로 나누기
    total = 0
    prev_number = 0

    for token in tokens:
        if token == 'Z':
            total -= prev_number  # "Z"가 나오면 바로 전에 더한 숫자를 빼기
        else:
            prev_number = int(token)  # 숫자일 경우 현재 숫자 저장
            total += prev_number

    return total
