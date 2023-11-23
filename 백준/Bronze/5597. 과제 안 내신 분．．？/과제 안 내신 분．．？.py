present_list = list(range(1,31))
unpresent_list = []

for _ in range (28):
    N = int(input())
    unpresent_list.append(N)
    
final_list = list(set(present_list) - set(unpresent_list))
print(min(final_list))
print(max(final_list))
    
    
