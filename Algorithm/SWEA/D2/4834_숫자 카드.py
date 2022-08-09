# 카운팅 정렬
T = int(input())

for t in range(1,T+1):
    N = int(input()) # 카드 장수
    cards = list(map(int, input())) # card의 숫자 리스트
    count = [0] * 10 # 카운팅을 할 리스트
    max_num, max_cnt = 0, 0 # 가장 많은 카드의 숫자, 최대 장수
    
    for idx in range(N): # 숫자들을 하나씩 카운팅
        count[cards[idx]] += 1
    
    for num in range(10): # 가장 많은 카드의 숫자와 비교하여 현재 숫자의 장수가 더 많을 경우 과 가장 많은 카드의 숫자와 최대 장수 변경
        if max_cnt <= count[num]: # 같거나 클 경우로 조건을 설정하여 적힌 숫자가 큰 쪽이 할당되도록 조건 설정
            max_num, max_cnt = num, count[num] 
    print(f'#{t} {max_num} {max_cnt}')