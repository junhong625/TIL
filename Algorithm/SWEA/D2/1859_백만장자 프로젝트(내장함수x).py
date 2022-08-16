T = int(input())

for t in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    max_num = -1
    total = 0
    while N_list and len(N_list) != 1: # 최대값 idx까지 순회하며 최대값과의 차이를 total에 더해주는 코드 
        max_num = 0
        for idx in range(len(N_list)):
            max_num = max_num if N_list[max_num] > N_list[idx] else idx
        for num in N_list[:max_num]:
            if N_list[max_num] > num:
                total += N_list[max_num] - num
        N_list = N_list[max_num+1:] 

    print(f'#{t} {total}')