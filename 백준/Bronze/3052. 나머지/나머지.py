percent = []

for _ in range (10):
    N = int(input())
    percent.append(N%42)
    
unique_remainders = set(percent)
print(len(unique_remainders))