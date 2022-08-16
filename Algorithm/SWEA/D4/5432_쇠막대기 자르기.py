T = int(input())

for t in range(1, T+1): 
    pipe = input()
    result = 0 # 총 파이프 개수
    pipe_cnt = 0 # 중첩 파이프 개수
    for i in range(len(pipe)): # 파이프 최대 길이만큼 순회
        if pipe[i] == '(': 
            if pipe[i+1] == '(': # '((' 가 나올 경우 중첩 파이프 개수 추가
                pipe_cnt += 1
            else: # '()' 경우 레이저도 판단하고 파이프 절단 
                result += pipe_cnt
        else: 
            if i+1 < len(pipe) and pipe[i+1] == ')': # '))' 경우 중첩 파이프 개수 감소, 닫은 파이프의 후미 부분 총 파이프 개수에 추가
                pipe_cnt -= 1
                result += 1
    print(result)