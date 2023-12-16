def solution(scores):
    result = []

    for i, (english, math) in enumerate(scores):
        rank = 1

        for j, (other_english, other_math) in enumerate(scores):
            if i != j and ((english + math) / 2) < ((other_english + other_math) / 2):
                rank += 1

        result.append(rank)

    return result