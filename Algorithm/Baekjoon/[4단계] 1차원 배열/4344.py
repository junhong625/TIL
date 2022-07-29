C = int(input())
for i in range(C):
    N_scores = list(map(int, input().split()))
    N = N_scores.pop(0)
    average = sum(N_scores) / N
    count = 0
    for score in N_scores:
        if score > average:
            count += 1
    print(f'{count/N*100:.3f}%')