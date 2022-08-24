T= int(input())

exchange = [50000, 10000, 5000, 1000, 500, 100, 50, 10] # 화폐 단위

for t in range(1, T+1):
    N = int(input())
    print(f'#{t}')
    for i in range(8):
        print(N // exchange[i], end=' ')    # 화폐 단위로 나눈 몫 출력
        N -= N // exchange[i] * exchange[i] # 금액 변경
    print()
