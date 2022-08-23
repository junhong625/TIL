for t in range(1, 11):
    N = int(input())
    N_list = input()
    stack = []
    cur = ''
    result = []
    cur2 = None
    
    for num in N_list:  # 중위 표기법을 후위 표기법으로 변경
        if not stack:
            stack.append(num)
        elif  num not in '+*':
            stack.append(num)
            stack.append(cur)
            if cur2:
                stack.append(cur2)
                cur2 = None
        else:
            if num == '*':
                if stack[-1] == '+':
                    cur = num
                    cur2 = stack.pop()
                else:
                    cur = num
            else:
                cur = num   
    
    for s in stack:
        if s != '*':
            result.append(s)
        else:
            a, b = int(result.pop()), int(result.pop())
            result.append(a*b)

    stack = []
    for s in result:
        if s != '+':
            stack.append(s)
        else:
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(a+b)
    print(f'#{t} {stack[0]}')
        