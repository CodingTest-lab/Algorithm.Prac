def solution(bin1, bin2):
    result = ''
    carry = 0

    # 두 이진수의 길이를 맞춰줍니다.
    while len(bin1) < len(bin2):
        bin1 = '0' + bin1
    while len(bin2) < len(bin1):
        bin2 = '0' + bin2

    # 뒤에서부터 각 자릿수를 더하고 결과를 구합니다.
    for i in range(1, len(bin1) + 1):
        sum_val = int(bin1[-i]) + int(bin2[-i]) + carry
        result = str(sum_val % 2) + result  # 현재 자릿수의 결과를 결과 문자열에 추가
        carry = sum_val // 2  # 올림 갱신

    # 마지막 덧셈이 끝나고 올림이 남아있을 경우 결과 문자열에 추가
    if carry > 0:
        result = str(carry) + result

    return result