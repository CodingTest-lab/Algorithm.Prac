def solution(quiz):
    result = []

    for expression in quiz:
        # 수식을 공백을 기준으로 나누어서 X, 연산자, Y, '=', Z로 분리
        parts = expression.split()
        X, operator, Y, equal, Z = parts

        # 문자열로부터 정수 값을 얻어내기
        X, Y, Z = int(X), int(Y), int(Z)

        # 정답 계산
        calculated_result = X + Y if operator == '+' else X - Y

        # 계산 결과와 주어진 Z가 일치하는지 확인하여 결과 리스트에 추가
        if calculated_result == Z:
            result.append("O")
        else:
            result.append("X")

    return result

# 예시 테스트
quiz1 = ["3 - 4 = -3", "5 + 6 = 11"]
result1 = solution(quiz1)
print(result1)  # ["X", "O"]

quiz2 = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]
result2 = solution(quiz2)
print(result2)  # ["O", "O", "X", "O"]
