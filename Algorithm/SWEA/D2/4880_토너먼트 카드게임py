def rsp(A, B):                  # 가위바위보 승자 결정
    if arr[A] - arr[B] == 1:    # 몇 번째 사람이 우승자인지 수월하게 알아내기 위해 index를 이용하여 값을 구하기
        return A
    elif arr[A] - arr[B] == -1:
        return B
    elif arr[A] - arr[B] == 2:
        return B
    elif arr[A] - arr[B] == -2:
        return A
    else:
        return A

def card_game(group, N):    # 카드 게임 시작
    if N == 3:              # 3명의 그룹이 짝지어질 경우 가위바위보
        return rsp(rsp(group[0], group[1]), group[2])
    elif N == 2:            # 2명의 그룹이 짝지어질 경우 가위바위보
        return rsp(group[0], group[1]) 
    else:                   # 4명 이상일 경우
        if N % 2 == 1:      # 인원 수가 홀수면 한쪽이 한명 더 많도록 그룹 분할
            return rsp(card_game(group[:N//2+1], N//2+1), card_game(group[N//2+1:], N//2))
        else:               # 인원 수가 짝수면 양쪽 균등하게 그룹 분할
            return rsp(card_game(group[:N//2], N//2), card_game(group[N//2:], N//2))

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    idx_list = [i for i in range(N)] # 몇 번째 사람이 일등인지 알아내기 위한 idx_list
    print(f'#{t} {card_game(idx_list, N)+1}')