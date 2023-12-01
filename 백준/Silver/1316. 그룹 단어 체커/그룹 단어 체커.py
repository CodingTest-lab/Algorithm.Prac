def is_group_word(word):
    visited = set()  # 이미 방문한 문자를 기록하기 위한 집합

    for i in range(len(word)):
        if word[i] not in visited:  # 처음 나타난 문자인 경우
            visited.add(word[i])
        else:
            if word[i] != word[i - 1]:  # 바로 앞 문자와 다르면 그룹 단어가 아님
                return False

    return True

def count_group_words(words):
    count = 0

    for word in words:
        if is_group_word(word):
            count += 1

    return count

# 입력 처리
N = int(input())
word_list = [input() for _ in range(N)]

# 결과 출력
result = count_group_words(word_list)
print(result)
