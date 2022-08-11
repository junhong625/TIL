T = int(input())

for t in range(1, T+1):
    P, A, B = map(int, input().split())
    cnt_list = []
    
    # 목표값을 찾는데까지 걸린 횟수를 A는 cnt_list[0]에, B는 cnt_list[1]에 저장 
    for target in A, B: # 코드를 간결하게 하기 위해 A, B를 순회하는 반복문 생성
        start, end, cnt, mid = 1, P, 0, 0
        
        while mid != target: # 중간값(mid)과 목표값(target)이 같아질 경우 종료
            mid = (start + end) // 2 # 중간값 재설정
            if mid > target: # 중간값이 목표값보다 클 경우
                end = mid
            else:
                start = mid # 중간값이 목표값보다 작거나 같을 경우
            cnt += 1 # 탐색 횟수
        cnt_list.append(cnt) # A와 B의 탐색 횟수 추가

    # 결과 출력
    print(f'#{t}', end=' ')    
    if cnt_list[0] < cnt_list[1]:
        print('A')
    elif cnt_list[0] > cnt_list[1]:
        print('B')
    else:
        print(0)