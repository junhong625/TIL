T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    table = []
    max_total = 0
    for _ in range(N):
        table.append(input().split())
    for j in range(N-M+1):
        for m in range(N-M+1):
            total = 0
            for k in range(M):
                for l in range(M):
                    total += int(table[j+k][m+l])
                    if total > max_total:
                        max_total = total
    print("#%d %d" %(i, max_total))