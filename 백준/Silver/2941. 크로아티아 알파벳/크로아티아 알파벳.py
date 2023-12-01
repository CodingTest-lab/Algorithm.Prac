word = input()
croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatian_alphabets:
    word = word.replace(i,'*')
    
print(len(word))