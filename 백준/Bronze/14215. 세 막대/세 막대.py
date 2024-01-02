a, b, c = map(int,input().split())
result = [a, b, c]
two_plus = sum(result) - max(result)
total = 0 

if max(result) >= two_plus:
    total = (2 * (two_plus)) - 1
    print(total)
elif max(result) < two_plus:
    total = max(result) + two_plus
    print(total)
