while True:
    A, B, C = map(int, input().split())
    
    if A == 0 and B == 0 and C == 0:
        break

    if A < B + C and B < A + C and C < A + B:
        if A == B and B == C and A == C:
            print('Equilateral')
        elif A == B or B == C or A == C:
            print('Isosceles')
        elif A != B and B != C and A != C:
            print('Scalene')
    else:
        print('Invalid')
