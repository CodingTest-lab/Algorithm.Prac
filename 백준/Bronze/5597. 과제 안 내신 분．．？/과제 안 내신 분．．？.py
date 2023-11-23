submitted_numbers = set()

# 28명의 학생이 제출한 출석번호를 입력받음
for _ in range(28):
    submitted_numbers.add(int(input()))

# 모든 학생의 출석번호는 1부터 30까지이므로, 전체 출석번호를 가진 집합을 만듦
all_numbers = set(range(1, 31))

# 제출하지 않은 학생의 출석번호를 찾음
not_submitted_numbers = all_numbers - submitted_numbers

# 찾은 출석번호 중 가장 작은 것을 출력
print(min(not_submitted_numbers))

# 그 다음으로 작은 출석번호를 출력
print(min(not_submitted_numbers - {min(not_submitted_numbers)}))
