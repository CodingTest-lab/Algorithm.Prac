def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    #bin을 쓰면은 영문자 두개가 나오기에 [2:] 자르는게 맞다. 
    return answer