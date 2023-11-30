word = input()
is_pel = True

for i in range (len(word)//2):
    if word[i] != word[-1-i] :
        is_pel = False
        break
        
if is_pel:
    print('1')
else:
    print('0')
     