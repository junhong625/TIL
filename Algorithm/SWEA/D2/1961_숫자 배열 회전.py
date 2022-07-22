from functools import reduce
 
T = int(input())
for i in range(1, T+1):
    N = int(input())
    table = []
    answer_90 = []
    answer_180 = []
    answer_270 = []
    for n in range(N):
        table.append(input().split())
    for j in range(N):
        result = ""
        for k in range(N-1, -1, -1):
            result += table[k][j]
        answer_90.append(result)
    for j in range(N-1, -1, -1):
        result_1 = ""
        result_2 = ""
        for k in range(N-1, -1, -1):
            result_1 += table[j][k]
        answer_180.append(result_1)
        for l in range(N):
            result_2 += table[l][j]
        answer_270.append(result_2)
    print("#%d" %i)
    for j in range(N):
        print("%s %s %s" %(answer_90[j], answer_180[j], answer_270[j]))
