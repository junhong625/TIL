# Algorithm_7💡
# 스택 응용

## 계산기1

> 문자열로 된 계산식이 주어질 때, 스택을 이용하여 계산식의 값을 계산 가능
> 

- 중위 표기법(infix notation)
    - 연산자를 피연산자의 가운데 표기하는 방법
    - ex) `A+B`
- 후위 표기법(postfix notation)
    - 연산자를 피연산자의 뒤에 표기하는 방법
    - ex) `AB+`

### 문자열 수식 계산의 일반적인 방법

1. 중위 표기법의 수식을 후위 표기법으로 변경한다.
    - 수식의 각 연산자에 대해서 우선 순위에 따라 괄호를 사용하여 다시 표현
    - 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동
    - 괄호를 제거
    - 알고리즘 구현
        
        ```python
        chars = input()
        
        def intopostfix(s):
            out_value = {'(': 3, '-':1, '+':1, '/':2, '*':2}
            in_value = {'(': 0, '-':1, '+':1, '/':2, '*':2}
        
            stack = []
            result = ''
        
            # 중위 표기법을 후위 표기법으로 변경
            for char in chars:
                if char.isdigit():
                    result += char
                elif char == ')':
                    while stack[-1] != '(':
                        result += stack.pop()
                    stack.pop()
                elif not stack or in_value[stack[-1]] < out_value[char]:
                    stack.append(char)
                elif stack and in_value[stack[-1]] >= out_value[char]:
                    while stack and in_value[stack[-1]] >= out_value[char]:
                        result += stack.pop()
                    stack.append(char)
            return result
        
        print(intopostfix(chars))
        ```
        
2. 후위 표기법의 수식을 스택을 이용하여 계산한다.
    - 알고리즘 구현
        
        ```python
        def intopostfix(s): # 중위 표기법을 후위 표기법으로 변경하는 함수
            out_value = {'(': 3, '-':1, '+':1, '/':2, '*':2}
            in_value = {'(': 0, '-':1, '+':1, '/':2, '*':2}
        
            stack = []
            result = ''
        
            for char in chars:
                if char.isdigit():
                    result += char
                elif char == ')':
                    while stack[-1] != '(':
                        result += stack.pop()
                    stack.pop()
                elif not stack or in_value[stack[-1]] < out_value[char]:
                    stack.append(char)
                elif stack and in_value[stack[-1]] >= out_value[char]:
                    while stack and in_value[stack[-1]] >= out_value[char]:
                        result += stack.pop()
                    stack.append(char)
            return result
        
        def postfix_calculator(s): # 후위 표기법을 계산하는 함수
            s = intopostfix(s)
            stack = []
            for char in s:
                if char.isdigit():
                    stack.append(int(char))
                else:
                    a, b = stack.pop(), stack.pop()
                    if char == '-':
                        stack.append(b - a)
                    if char == '+':
                        stack.append(b + a)
                    if char == '*':
                        stack.append(b * a)
                    if char == '/':
                        stack.append(b / a)
            return stack[0]
        
        chars = input()
        print(postfix_calculator(chars))
        ```
        

# 백트래킹

> 해를 찾는 도중에 ‘막히면’ 되돌아가서 다시 해를 찾아 가는 기법
> 
- 최적화(optimization)문제와 결정(dicision)문제를 해결 가능
    - 결정 문제 : 문제의 조건을 만족하는 해가 존재하는지 여부를 ‘yes’ 또는 ‘no’가 답하는 문제
        - 미로 찾기
        - n-Queen 문제
        - Map coloring
        - 부분 집합의 합(Subset Sum) 문제 등

## 백트래킹과 DFS의 차이

- 경로가 해결책으로 이어질 것 같지 않으면 가지 않음으로써 시도의 횟수를 줄임(Prunning: 가지치기)
- DFS는 모든 경로를 추적, 백트래킹은 불필요한 경로 조기에 차단
- DFS를 하기에는 경우의 수가 너무나 많음 즉, N!가지의 경우의 수를 가진 문제에 대해 DFS는 당연히 적용 불가능한 문제
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 최악의 경우 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능

### N-Queen 예시

- DFS 탐색 시 → 155 노드 탐색
- 백트래킹 탐색 시 → 27 노드 탐색

> DFS보다 더욱 효율적으로 탐색이 가능
> 

## 백트래킹의 절차

1. 상태 공간 트리의 DFS을 실시
2. 각 노드가 유망(promising)한지를 점검
3. 만일 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.

## 백트래킹 기법으로 부분 집합 구하기

- n개의 원소가 들어있는 집합의 2**n개의 부분 집합을 만들 때는, True 또는 False 값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용
- 여기서 배열의 i번째 항목은 i번째의 원소가 부분 집합의 값인지 아닌 지를 나타내는 값
- 알고리즘 구현
    - 모든 부분 집합을 구하는 경우
        
        ```python
        def f(i:int, N:int): # i: index, N: 원소의 개수
            global cnt
            cnt += 1
            if i == N:              
                print([a[i] for i in range(N) if bit[i]]) # 모든 부분 집합 출력
            else:
                bit[i] = 1
                f(i+1, N)
                bit[i] = 0
                f(i+1, N)
            
        
        a = [i for i in range(1, 11)]
        bit = [0] * len(a)
        cnt = 0 # 작업 횟수
        f(0, len(a))
        print(answer, cnt)
        ```
        
    - 부분 집합의 합을 구하는 경우
        
        ```python
        def f(i:int, N:int, s:int, t:int):
            global answer
            global cnt
            cnt += 1
            if i == N:
                if s == t:              # 부분 집합의 합이 t일 경우
                    answer += 1
                return                  # 모든 원소가 고려된 경우
            elif s > t:
                return 
            else:                   
                f(i+1, N, s+a[i], t)    # a[i]가 합에 포함된 경우
                f(i+1, N, s, t)         # a[i]가 합에 포함되지 않은 경우
        
        a = [i for i in range(1, 11)]
        bit = [0] * len(a)
        answer = 0
        cnt = 0
        f(0, len(a), 0, 5)
        print(answer, cnt)
        ```
        

## 백트래킹으로 순열 구하기

```python
def f(i, N):
    if i == N:       # 순열 완성
        print(p)
    else:
        for j in range(i, N): # p[i]에 들어갈 숫자 p[j]결정
            p[i], p[j] = p[j], p[i] # p[i]와 p[j]를 치환
            f(i+1, N)               # 치환된 상태의 p를 재귀 적용
            p[i], p[j] = p[j], p[i] # 원래대로 치환

p = [1,2,3]
f(0, len(p))
```