def solution(array):
    count = 0
    result = ''
    for i in range(len(array)):
        result += str(array[i])
    for x in range(len(result)):
        if result[x] == '7':
            count += 1
    return count
