str = input()
str1 = str.upper()
str2 = str.lower()
result = ''

for i in range (len(str)):
    if str[i] != str1[i]:
        result += str1[i]
    elif str[i] != str2[i]:
        result += str2[i]

print(result)

