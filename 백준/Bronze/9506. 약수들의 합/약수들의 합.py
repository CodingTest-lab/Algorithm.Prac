while True:
    n = int(input())
    list_m = []

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            list_m.append(i)

    if n == sum(list_m):
        print(f'{n} = ' + " + ".join(map(str, list_m)))
    else:
        print(f'{n} is NOT perfect.')
