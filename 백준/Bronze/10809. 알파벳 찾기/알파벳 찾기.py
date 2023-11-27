word = input()
positions = [-1]*26

for i in range (len(word)):
    index = ord(word[i])-ord('a')
    
    if positions[index] == -1:
        positions[index] = i
        
print(' '.join(map(str, positions)))
    