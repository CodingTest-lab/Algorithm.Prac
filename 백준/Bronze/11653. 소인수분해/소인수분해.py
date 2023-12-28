def prime_factorization(N):
    result = []
    for i in range(2, N + 1):
        while N % i == 0:
            N //= i
            result.append(i)
    
    return result

N = int(input())
result = prime_factorization(N)

for factor in result:
    print(factor)