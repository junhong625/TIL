N = int(input())
scores = list(map(int, input().split()))
max_score = scores.pop(scores.index(max(scores)))
for i in range(len(scores)):
    scores[i] = scores[i]/max_score*100
print((sum(scores) + 100) / N)