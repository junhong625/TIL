T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    q = []  # 화덕
    cnt = 0 # 채워진 화덕 개수
    idx = 1 # 현재 피자 번호
    
    # 화덕에 피자 삽입
    for _ in range(N):
        if Ci:
            q.append((Ci.pop(0), idx))  # 피자 삽입
            idx += 1
            cnt += 1

    # 화덕에 피자가 하나 남을 때까지 반복
    while cnt != 1:
        for _ in range(N):  # 한 바퀴를 돌며 
            cheeze, i = q.pop(0) 
            if cheeze//2 > 0:   # 치즈가 완전히 녹지 않았을 경우
                q.append((cheeze//2, i)) # 다시 삽입
            else:   # 치즈가 모두 녹았을 경우
                cnt -= 1 # 빈 화덕이 하나 생김
                break
        if Ci and cnt < N: # 피자가 남아 있을 경우
            q.append((Ci.pop(0), idx))  # 피자 삽입
            idx += 1
            cnt += 1
    print(f'#{t} {q[0][1]}')
    
    # 피자를 모두 화덕에 집어넣었을 때까지 반복해본 후 
    # 치즈양/2에 대한 몫이 가장 큰 피자가 마지막이라고 지정했을 경우 반례 발생
    # 13, 10 이 남아있을 경우 결국엔 10이 가장 마지막에 나오게 되지만 
    # 그냥 치즈양/2를 하여 몫이 가장 큰 피자를 출력할 경우 13이 출력 됨
    #
    #         q.append((cheeze//2, i)) # 다시 삽입
    # max_cheeze = 0  # 가장 많은 치즈 양
    # last_pizza = 0  # 가장 많은 치즈 양을 가진 피자 번호
    
    # for cheeze, i in q: # 남아있는 피자 중에 / 2를 했을 경우 치즈가 가장 많이 남은 피자의 번호를 출력 
    #     if cheeze//2 >= max_cheeze:
    #         max_cheeze, last_pizza = cheeze//2, i
    # print(f'#{t} {last_pizza}')