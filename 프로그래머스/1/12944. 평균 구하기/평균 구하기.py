def solution(arr):
    result = 0
    for x in range (len(arr)):
        result += arr[x]
    
    middle_gap = result / len(arr)
    return middle_gap

# sum(arr) / len(arr) = result해서 출력해도 된다.
        