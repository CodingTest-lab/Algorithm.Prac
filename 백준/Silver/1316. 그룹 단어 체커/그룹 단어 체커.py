num = int(input())
count = 0

for _ in range (num):
    word = input()
    for i in range (len(word)-2): 
        if word[i] != word[i+1] and word[i] in word[i+2:]:
            count += 1
            break
            
print(num - count)