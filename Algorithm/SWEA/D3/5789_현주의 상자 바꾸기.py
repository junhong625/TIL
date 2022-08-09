T = int(input()) # 테스트 케이스 수 할당

for t in range(1, T+1): # 테스트 케이스 수 만큼 반복
    N, Q = map(int,input().split()) # 상자 개수, 변경할 횟수
    boxes = [0 for _ in range(N)] # list comprehension으로 상자 개수만큼 0이 있는 리스트 생성
    
    for q in range(1, Q+1): # 변경할 횟수만큼 반복
        L, R = map(int,input().split()) # L, R 할당
        
        for i in range(L-1,R): # L과 R값은 인덱스 보다 1씩 크기에 그에 맞춰 범위를 설정
            boxes[i] = q # L,R 범위에 있는 박스 숫자 변경
    
    print(f'#{t}', end=' ')
    for i in range(N):
        print(boxes[i], end=' ')
    print()