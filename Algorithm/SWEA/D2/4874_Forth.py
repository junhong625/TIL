T = int(input())

for t in range(1, T+1):
    postfix = list(map(str, input().split()))
    stack = []
    cnt = 0
    for i in postfix:
        if i == '.':
            break
        elif i not in '*+-/':   # 숫자일 경우
            stack.append(i)
            cnt += 1
        else:                   # 연산자일 경우
            if cnt >= 2:        # 스택에 두개 이상 존재할 경우
                a, b = int(stack.pop()), int(stack.pop())
                cnt -= 2

                # 각 연산자에 맞는 연산 실행
                if i == '*':    
                    stack.append(str(b * a))
                    cnt += 1
                elif i == '+':
                    stack.append(str(b + a))
                    cnt += 1
                elif i == '-':
                    stack.append(str(b - a))
                    cnt += 1
                else:
                    stack.append(str(b // a))
                    cnt += 1

            else: # 스택이 2개 이하인 경우에 연산자가 나올 시 오류
                stack.append('error')
                cnt += 1
                break
    if cnt > 1: # 작업이 끝난 후 결과값만 있어야할 stack의 길이가 1보다 클 경우 오류
        print(f'#{t} error')
    elif cnt == 1: # 작업이 끝난 후
        if 'error' in stack:    # stack에 들어있는 원소가 'error'일 경우
            print(f'#{t} error')
        else:                   # stack에 정상적인 원소가 들어있는 경우
            print(f'#{t} {stack[0]}')
    else:                       # stack에 들어있는 것이 없는 경우
        print(f'#{t} error')