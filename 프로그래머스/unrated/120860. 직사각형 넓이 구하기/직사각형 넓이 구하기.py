def solution(dots):
    x_values = [x for x,y in dots]
    y_values = [y for x,y in dots]
    
    min_x, max_x= min(x_values), max(x_values)
    min_y, max_y= min(y_values), max(y_values)
    
    a = max_x - min_x
    b = max_y - min_y
    
    area = a * b
    
    return area