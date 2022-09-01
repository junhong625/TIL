import sys

sys.stdin = open('ssafy-algorithm/0819/1952_수영장/input.txt', 'r')


T = int(input())

for t in range(1, T+1):
    payment = list(map(int, input().split()))
    month = list(map(int, input().split())) + [0,0]
    

    idx = 0
    total, total2 = 0, 0
    while idx < 12: # 경우의 수를 계산하여 3달 계산이 작을 경우에만 3칸 이동
        if month[idx] == 0:
            idx += 1
            continue
        sub_tot = 0
        for i in range(idx, idx+3):
            sub_tot += month[i] * payment[0] if month[i] * payment[0] < payment[1] else payment[1]
        if sub_tot < payment[2]:
            
            
            for j in range(idx, idx+3):
                sub_sub_tot = 0
                for k in range(j, j+3):
                    sub_sub_tot += month[i] * payment[0] if month[i] * payment[0] < payment[1] else payment[1]
                if sub_sub_tot > payment[2]:
                    idx += 3
            
            
            total += month[idx] * payment[0] if month[idx] * payment[0] < payment[1] else payment[1]
            idx += 1
        else:
            total += payment[2]
            idx += 3

    # idx = 0
    # while idx < 12: # 경우의 수를 계산하여 계속 3칸 이동
    #     if month[idx] == 0:
    #         idx += 1
    #         continue
    #     sub_tot = 0
    #     for i in range(idx, idx+3):
    #         sub_tot += month[i] * payment[0] if month[i] * payment[0] < payment[1] else payment[1]
    #     if sub_tot < payment[2]:
    #         total2 += sub_tot
    #         idx += 3
    #     else:
    #         total2 += payment[2]
    #         idx += 3

    # total = total if total < total2 else total2

    print(f'#{t} {total if total < payment[3] else payment[3]}')