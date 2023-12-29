x_coords = []
y_coords = []

for _ in range(3):
    x, y = map(int, input().split())
    x_coords.append(x)
    y_coords.append(y)

fourth_x = 0
fourth_y = 0

for x in x_coords:
    if x_coords.count(x) == 1:
        fourth_x = x

for y in y_coords:
    if y_coords.count(y) == 1:
        fourth_y = y


print(f"{fourth_x} {fourth_y}")
