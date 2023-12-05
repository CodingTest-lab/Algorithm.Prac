full_paper = [[0] * 100 for _ in range(100)]

num_paper = int(input())

for _ in range(num_paper):
    l, b = map(int, input().split())

    for i in range(b, b + 10):
        for j in range(l, l + 10):
            full_paper[i][j] = 1

black_paper_count = sum(x.count(1) for x in full_paper)

print(black_paper_count)
