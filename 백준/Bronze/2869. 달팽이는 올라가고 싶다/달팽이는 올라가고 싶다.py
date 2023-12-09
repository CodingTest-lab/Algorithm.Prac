A,B,V = map(int,input().split())

day = (V-B)/(A-B)
i = (V-B)%(A-B)

if i == 0:
    print(int(day))
elif i != 0:
    print(int(day) + 1)