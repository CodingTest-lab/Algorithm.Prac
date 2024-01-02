N = int(input())
A = []
B = []


for _ in range (N):
    x,y = map(int, input().split())
    A.append(x)
    B.append(y)
    
if N == 1:
    print(0)
else:        
    result = (max(A) - min(A)) * (max(B) - min(B))
    print(result)