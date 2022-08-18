import sys

n = int(sys.stdin.readline())
stack = [i for i in range(1, n+1)]
done = []
cur_num = 1
for _ in range(1,n+1): # n만큼 숫자 입력 받기
    num = int(sys.stdin.readline())
    if num > cur_num: # 다음 행동 숫자보다 입력 받은 숫자가 클 경우
        while cur_num <= num: # cur_num이 num보다 커질 때까지 반복 
            stack.append(cur_num)# cur_num을 stack에 추가 
            cur_num += 1 # 다음 숫자로 이동       
            done.append('+') # 행동 추가
        stack.pop()  # stack에서 num에 해당하는 숫자 제거
        done.append('-') # 행동 추가

    elif num == cur_num: # 다음 행동 숫자와 입력 숫자가 같을 경우
        done.append('+') # 행동 추가 
        done.append('-') # 행동 추가
        cur_num += 1 # 다음 숫자로 이동

    else: # 다음 행동 숫자가 입력 숫자보다 작을 경우
        if num == stack[-1]: # 입력 받은 숫자가 stack의 마지막 수와 같을 경우
            stack.pop() # stack에서 num에 해당하는 숫자 제거
            done.append('-') # 행동 추가
        else:
            done.append('NO') # 작업이 안될 경우 'NO'추가
if 'NO' in done: # done에 'NO'가 있을 경우 'NO'만 출력
    print('NO')
else: # 모든 행동 출력
    for d in done:
        print(d)
