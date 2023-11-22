N = int(input())
numbers = list(map(int, input().split()))

sorted_numbers = sorted(numbers)
print(sorted_numbers[0], sorted_numbers[N-1])
