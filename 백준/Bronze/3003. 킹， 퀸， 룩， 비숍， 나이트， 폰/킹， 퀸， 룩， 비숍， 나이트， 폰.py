piece = list(map(int,input().split()))
o_piece = [1,1,2,2,2,8]

e_element = [x - y for x, y in zip(o_piece,piece)]
print(*e_element)