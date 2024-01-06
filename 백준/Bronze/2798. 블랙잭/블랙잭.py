N, M = map(int, input().split())
cards = [int(x) for x in input().split()]
Num = len(cards)
combination = []

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            combination.append((cards[i], cards[j], cards[k]))

closest_sum = float('inf')

for comb in combination:
    current_sum = sum(comb)
    if current_sum <= M and abs(M - current_sum) < abs(M - closest_sum):
        closest_sum = current_sum

print(closest_sum)
