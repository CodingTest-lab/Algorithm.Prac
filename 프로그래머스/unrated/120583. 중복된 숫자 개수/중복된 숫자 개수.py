def solution(array, n):
    count = 0
    for i in range (len(array)):
        if n == array[i]:
            count +=1
    return count
    