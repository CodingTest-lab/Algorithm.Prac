N = int(input())
result = ''

if N % 4 == 0:  
    for _ in range(1, (N//4)+1):  
        result += 'long '

    print(result + 'int')
