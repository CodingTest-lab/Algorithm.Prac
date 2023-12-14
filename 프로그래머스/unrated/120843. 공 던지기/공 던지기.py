def solution(numbers, k):
    result = numbers[0] + ((k - 1) * 2)
    for _ in range(500):
        if result > len(numbers):
            result -= len(numbers)
        elif result <= len(numbers):
            return result
        else:
            return result
        
        
        #if result > len(numbers):
        #for i in numbers:
         #   if result != i:
          #      result -= len(numbers)
    #return result