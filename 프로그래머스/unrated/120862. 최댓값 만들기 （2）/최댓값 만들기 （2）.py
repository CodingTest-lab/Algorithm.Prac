def solution(numbers):
    numbers.sort()

    if len(numbers) < 2:
        return "List should contain at least two numbers."

    max_num = max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
    
    return max_num
