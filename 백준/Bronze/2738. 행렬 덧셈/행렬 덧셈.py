N,M = map(int,input().split())

matrix_a = [list(map(int,input().split())) for _ in range(N)]
matrix_b = [list(map(int,input().split())) for _ in range(N)]

result_matrix = [[0] * M for _ in range(N)]

for i in range (N):
    for j in range (M):
        result_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]
     
for row in result_matrix:
    print(*row)