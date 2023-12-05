matrix_a = [list(map(int,input().split())) for _ in range(9)]
max_value = float('-inf')  #음수 무한대로 가정
max_row, max_column = 0, 0
for i in range (len(matrix_a)):
    for j in range(len(matrix_a[i])):
        if matrix_a[i][j] >= max_value:
            max_value = matrix_a[i][j]
            max_row = i
            max_column = j

print(max_value)
print(max_row +1, max_column +1)