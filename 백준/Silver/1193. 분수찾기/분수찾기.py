X = int(input())

line = 1  # 대각선의 번호
while X > line:
    X -= line
    line += 1

# 대각선의 번호(line)이 홀수인 경우와 짝수인 경우를 나누어서 계산
if line % 2 == 1:
    numerator = line - X + 1
    denominator = X
else:
    numerator = X
    denominator = line - X + 1

print(f"{numerator}/{denominator}")