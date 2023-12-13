def solution(slice, n):
    pizzas = n / slice
    if n % slice > 0:
        return int(pizzas)+1
    elif n % slice == 0:
        return int(pizzas)