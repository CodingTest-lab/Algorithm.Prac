numbers = []  

for i in range(1, 10):  
    A = int(input())
    numbers.append(A)  

print(max(numbers))  

max_index = numbers.index(max(numbers))
print(max_index + 1)  
