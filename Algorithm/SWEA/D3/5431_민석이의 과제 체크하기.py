T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    st = [False] * N                            # 과제 제출한 학생들을 체크할 리스트
    good_st = list(map(int, input().split()))   
    for g in good_st:                           # 과제를 제출한 학생들은 True로 변경               
        st[g-1] = True

    print(f'#{t}', end=' ')
    for i in range(N):                          # 과제를 제출하지 않은 학생들 번호 출력
        if not st[i]:
            print(i+1, end=' ')
    print()