words = [input() for _ in range(5)]

result = ''

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            result += words[i][j]

print(result)
