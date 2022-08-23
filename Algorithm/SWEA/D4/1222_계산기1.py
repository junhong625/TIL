for t in range(1, 11):
    N = int(input())
    N_list = input()
    stack = []
    cur = ''
    result = []
    
    for num in N_list:  # 중위 표기법을 후위 표기법으로 변경
        if not stack:
            stack.append(num)
        elif  num != '+':
            stack.append(num)
            stack.append(cur)
        else:
            cur = num
            
    for s in stack:     # 후위 표기법을 계산
        if s != '+':
            result.append(s)
        else:
            a, b = int(result.pop()), int(result.pop())
            result.append(a + b)
    print(f'#{t} {result[0]}')