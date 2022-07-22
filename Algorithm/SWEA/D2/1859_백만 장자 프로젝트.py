T = int(input())
for i in range(1, T+1):
    total = 0
    total_m = 0
    count = 0
    N = int(input())
    N_list = list(map(int, input().split()))
    if N_list == sorted(N_list):
        print(f'#{i} {N_list[-1] * len(N_list[:-1]) - sum(N_list[:-1])}')
        continue
    elif N_list == sorted(N_list, reverse=True):
        print(f'#{i} 0')
        continue
    else:
        max_n = max(N_list)
        for j in range(N):
            if N_list[j] != max_n:
                total_m += N_list[j]
                count += 1
            else:
                total += count * max_n - total_m
                total_m = 0
                count = 0
                if j != N-1:
                    max_n = max(N_list[j+1:]) 
        print(f'#{i} {total}')


