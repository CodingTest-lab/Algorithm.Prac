def solution(hp):
    generals = hp // 5
    soldiers = (hp % 5) // 3
    remaining_hp = (hp % 5) % 3

    ants = generals + soldiers + remaining_hp

    return ants