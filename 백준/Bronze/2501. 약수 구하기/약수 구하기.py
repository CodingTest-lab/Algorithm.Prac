N,K = map(int, input().split())
list_m = []    
    
for i in range(1, N+1):
    if N % i == 0:
        list_m.append(i)
        
if K <= len(list_m):
    print(list_m[K - 1])
else:
    print(0)