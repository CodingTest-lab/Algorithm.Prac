X = int(input())
N = int(input())
total = 0

for _ in range(1, N+1):
    a, b = map(int, input().split())
    total += (a * b)

if X == total:
    print('Yes')
else:
    print('No')
