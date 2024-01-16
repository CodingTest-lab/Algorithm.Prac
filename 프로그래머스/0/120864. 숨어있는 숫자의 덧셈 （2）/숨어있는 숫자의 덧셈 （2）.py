def solution(my_string):
    total = 0
    current = 0
    
    for i in my_string:
        if i.isdigit():
            current = current * 10 + int(i)
        else:
            total += current
            current = 0
    
    return total+current 
        