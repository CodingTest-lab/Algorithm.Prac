def solution(spell, dic):
    for word in dic:
        if sorted(spell) == sorted(word):
            return 1
    return 2
