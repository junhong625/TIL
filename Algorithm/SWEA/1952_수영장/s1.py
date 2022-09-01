import sys

sys.stdin = open('ssafy-algorithm/0819/1952_수영장/input.txt', 'r')


T = int(input())

for t in range(1, T+1):
    payment = list(map(int, input().split()))
    month = list(map(int, input().split())) + [0,0]
    
    idx = 0
    total = 0
    while idx < 12:
        # print(total, idx)
        dp = month[idx] * payment[0]
        if dp < payment[1] and dp < payment[2]: # 일요금으로 계산한 값이 월, 월3 보다 낮을 경우
            total += dp                         # 일요금으로 게산
            idx += 1
            continue
        else:                                   # 월, 월3보다 낮지 않을 경우
            next_dp = month[idx+1] * payment[0] # 다음날의 일요금 계산

            if next_dp < payment[1] and next_dp < payment[2]: # 다음날의 계산값이 월, 월3 보다 낮을 경우
                sub_tot = 0
                for i in range(idx, idx+3):
                    sub_tot += month[i] * payment[0] if month[i] * payment[0] < payment[1] else payment[1]
                if sub_tot <= payment[2]:
                    total += payment[1]
                    idx += 1 
                else:
                    total += payment[2]
                    idx += 3
                # if payment[1] < payment[2]:     # 월, 월3보다 더 낮은 값을 현재 요일에 계산
                #     total += payment[1]
                #     idx += 1
                #     continue
                # else:
                #     total += payment[2]
                #     idx += 3
                #     continue
            else:
                total += payment[2]
                idx += 3

    print(f'{t} {total if total < payment[3] else payment[3]}')