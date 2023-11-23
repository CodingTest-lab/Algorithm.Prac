N = int(input())
pre_score = list(map(int,input().split()))

max_score = max(pre_score)
new_score = [score / max_score * 100 for score in pre_score]

average = sum(new_score) / N 
print(average)