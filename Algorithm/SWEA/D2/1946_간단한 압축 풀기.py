T=int(input())
for i in range(1, T+1):
    answer = ""
    N=int(input())
    for j in range(N):
        alphabet, count = map(str, input().split())
        answer += alphabet * int(count)
    print('#%d' %i)
    if len(answer) % 10 == 0:
        for k in range(len(answer)//10):
            print(answer[k*10:(k+1)*10])
    else:
        for k in range(len(answer)//10+1):
            print(answer[k*10:(k+1)*10])