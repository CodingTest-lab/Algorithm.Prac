def solution(array, n):
    t_list = [ ]
    array.sort()
    for i in range (len(array)):
        if n >= array[i]:
            t_list.append(n-array[i])
        elif n < array[i]:
            t_list.append(array[i]-n)
    
    
    x = t_list.index(min(t_list))
    return array[x]
            