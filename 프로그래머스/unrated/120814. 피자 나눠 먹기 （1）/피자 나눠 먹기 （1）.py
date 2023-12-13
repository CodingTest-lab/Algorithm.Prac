def solution(n):
    pizzas = n / 7
    if n % 7 > 0:
        return int(pizzas)+1
    elif n% 7 ==0:
        return int(pizzas)