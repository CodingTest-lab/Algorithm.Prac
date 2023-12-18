from math import comb

def solution(balls, share):
    result = comb(balls, share)
    return result

#combination(즉 조합)은 from math import comb해서 쓸수 있다. 