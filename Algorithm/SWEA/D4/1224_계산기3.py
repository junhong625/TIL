def intopostfix(s):
    out_value = {'(': 3, '-':1, '+':1, '/':2, '*':2}
    in_value = {'(': 0, '-':1, '+':1, '/':2, '*':2}

    stack = []
    result = ''

    # 중위 표기법을 후위 표기법으로 변경
    for char in s:
        if char.isdigit():                                          # 문자가 피연산자인지 확인
            result += char                                          # 숫자라면 result에 문자로 더해준다
        elif char == ')':                                           # 문자가 닫는 괄호인지 확인
            while stack[-1] != '(':                                 # stack에서 여는 괄호가 나올 때까지 pop 
                result += stack.pop()
            stack.pop()
        elif not stack or in_value[stack[-1]] < out_value[char]:    # stack이 비어있거나 들어오는 연산자의 우선순위가 stack의 마지막 연산자보다 클 경우 stack에 추가 
            stack.append(char)
        elif stack and in_value[stack[-1]] >= out_value[char]:      # stack에 원소가 존재하거나 들어오는 연산자의 우선순위가 stack의 마지막 연산자와 같거나 보다 작은 경우
            while stack and in_value[stack[-1]] >= out_value[char]: # stack에서 더 작은 우선 순위의 연산자가 나올 때까지 pop
                result += stack.pop()                               
            stack.append(char)                                      # 작업을 끝낸 후 새로운 연산자 삽입

    while stack:                                                    # 작업 후 남은 연산자 추가
        result += stack.pop()
    return result

def postfix_calculator(s): # 후위 표기법을 계산하는 함수
    s = intopostfix(s)                      # 중위 표기법으로 저장된 문자열을 후위 표기법으로 변환
    stack = []
    for char in s:                         
        if char.isdigit():                  # 피연산자인지 확인
            stack.append(int(char))
        else:                               # 연산자일 경우
            a, b = stack.pop(), stack.pop() # stack에서 피연산자 2개를 pop 

            if char == '-':                 # 현재 연산자에 따라 피연산자 2개의 연산을 결정 
                stack.append(b - a)
            if char == '+':
                stack.append(b + a)
            if char == '*':
                stack.append(b * a)
            if char == '/':
                stack.append(b / a)
    return stack[0]                         # 계산을 끝낸 후 남은 결과값 반환

for t in range(1, 11):
    N = int(input())
    chars = input()
    print(f'#{t} {postfix_calculator(chars)}')
