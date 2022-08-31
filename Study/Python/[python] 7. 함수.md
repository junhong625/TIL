# Python_7 🖥️

# 함수

- 함수를 왜 사용할까요?
    - Decomposition(분해)
    - Abstraction(추상화)
    

### 분해(Decomposition)

> **기능을 분해하고 재사용 가능하게 만듦**
> 

### 추상화(Abstraction)

> **복잡한 내용을 모르더라도 사용할 수 있도록 재사용성과 가독성, 생산성**
> 
- 내부 구조를 변경할게 아니라면 내부 구조를 몰라도 무방

## 함수 기초

- 함수는 크게 3가지로 분류
    1. 내장 함수
        - 파이썬에 기본적으로 포함된 함수
    2. 외장 함수
        - import 문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
    3. 사용자 정의 함수
        - 직접 사용자가 만드는 함수
        

## 함수의 정의

- 함수(Function)
    - 특정한 기능을 하는 코드의 조각(묶음)
    - 특정 코드를 매번 다시 작성하지 않고, 필요 시 호출하여 간편히 사용
    

## 함수의 기본 구조

- 선언(생성)과 호출(사용) = (define & call)
- 입력(Input)
- 문서화(Docstring)
- 범위(Scope)
- 결과값(Output)

### 선언과 호출(define & call)

- 함수의 선언은 `def` 키워드를 활용함
- 들여쓰기를 통해 `Function body`(실행될 코드 블록)를 작성함
    - `Docstring`은 함수 `body` 앞에 선택적으로 작성 가능
        - 작성 시에는 반드시 첫 번째 문장에 문자열 ``````
- 함수는 `parameter`를 넘겨줄 수 있음
- 함수는 동작 후에 `return`을 통해 결과값을 전달함
- `parameter` 는 함수 정의 할 때의 변수

## 함수 사용 방법

- 함수를 사용하기 위해서는 먼저 함수를 정의해야 함
    
    ```python
    def function_name(parameters):
        '''Docstring'''
        # function body
        return # result    
    ```
    

# 함수의 결과값(Output)

## 값에 따른 함수의 종류

- Void function
    - 명시적인 `return` 값이 없고 `None`을 반환
    - ex) `print()` ⇒ 값을 출력하지만 값을 반환 X
- Value returning function
    - 함수 실행 후, `return`문을 통해 값 반환
    - `return` 시 값 반환 후 함수 종료

### print함수와 return의 차이점

- print를 사용하면 호출될 때마다 값이 출력 됨(주로 테스트에 이용)
- 데이터 처리를 위해서는 return을 사용

```python
# print 함수
void_function(a, b):
    print(f'{a} + {b} = {a + b}')

ans = void_function(1, 2)
print(ans)

# None
```

```python
# print 함수
void_function(a, b):
    return a + b

ans = void_function(1, 2)
print(ans)

# 3
```

## 두 개 이상의 값 반환

### 튜플(tuple) 활용

```python
def minus_and_product(x, y):
    return x - y, x * y 

a = minus_and_product(5, 2)
print(a)

# 3, 10
```

## 함수 반환 정리

- `return`이 없을 경우 ⇒ `None`
- `return`이 있을 경우 ⇒ 하나를 반환
- 여러 개의 `return`을 원할 경우 ⇒ `Tuple` 활용(리스트와 같은 컨테이너 사용도 가능)

## 함수의 입력

Argument : 함수를 **호출할 때** 넣어주는 값

Parameter : 함수를 **정의할 때** 함수 내부에서 사용되는 변수

### Argument란?

- 함수 호출 시 함수의 parameter를 통해 전달되는 값
- Argument는 소괄호 안에 할당 ⇒ func_name(argument)
    - 필수 Argument : 반드시 전달되어야 하는 argument
    - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본값이 전달
    

### Positional Arguments

- 기본적으로 함수 호출 시 Argument는 위치에 맞춰서 함수 내에 전달됨

```python
def add(x, y):
    return x + y

add(2, 3) # x = 2, y = 3
```

### Keyword Arguments

- 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
- Keyword Argument 다음에 Positional Argument를 사용할 수 없음

```python
def add(x, y):
    return x + y

add(x=2, y=5) # O
add(2, y=5) # O
add(x=2, 5) # X -> Error 발생
```

### Default Arguments Values

- 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
    - 정의된 것보다 더 적은 개수의 argument들로 호출 가능

```python
def add(x, y=0):
    return x + y

add(2) # add(x=2, y=0)
```

### 정해지지 않은 여러 개의 Argument 처리

- 애스터리스크(Asterisk) 혹은 언패킹 연산자인 `*` 사용
- 가변인자 `(*args)`
    - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
    - 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용
    

### 패킹 / 언패킹

- 가변 인자를 이해하기 위해서는 패킹, 언패킹을 이해해야 함
- 패킹
    - 여러 개의 데이터를 묶어서 변수에 할당하는 것
    
    ```python
    numbers = (1, 2, 3, 4, 5) # 패킹
    ```
    
- 언패킹
    - 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
    - 언패킹 시 변수의 개수와 할당하고자 하는 요소의 개수가 동일해야 함
    
    ```python
    numbers = (1, 2, 3, 4, 5)
    a, b, c, d, e = numbers # 언패킹
    a, b, c, d, e, f = numbers
    # ValueError: not enough to values to unpack (excepted 6, got 5)
    ```
    
    - 왼쪽의 변수에 `asterisk(*)` 를 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음
    
    ```python
    numbers = (1, 2, 3, 4, 5)
    
    a, b, *rest = numbers
    print(rest) # [3, 4, 5]
    
    a, *rest, e = numbers
    print(rest) # [2, 3, 4]
    ```
    

### Asterisk (*)와 가변 인자

- `*`는 스퀸스 언패킹 연산자라고도 불리며, 말 그대로 시퀀스를 풀어 헤치는 연산자
    - 주로 튜플이나 리스트를 언패킹하는데 사용
    - `*`를 활용하여 가변 인자를 만들 수 있음
        - 이름은 자유롭게 생성
    
    ```python
    def sum_all(*numbers):
        result = 0
        for num in numbers:
            result += num
        return result
    
    print(sum_all(1, 2, 3)) # 6
    print(sum_all(1, 2, 3, 4, 5, 6)) # 21
    ```
    

### 가변 키워드 인자(**kwargs)

- 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
- `**kwargs`는 **딕셔너리로 묶여 처리**되며, `parameter`에 `**`를 붙여 표현

```python
def family(**kwasrgs):
    for key, value in kwargs.items():
    print(key, ":", value)

family(father = '아부지', mother = '어무이, baby = '아기') # key = 문자열 X
```

### 가변 인자(**args)와 가변 키워드 인자(***kwargs) 동시 사용 예시

- 가변 인자와 가변 키워드 인자를 함께 사용할 수 있음
- 키워드로 넣은 인자는 키워드로 분류 되기에 구분 가능

```python
def print_family_name(*parents, **pets):
```

# 함수 응용

## 내장 함수(Built-in Functions)

- 파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수와 형(type)이 있음

### map

> map(function, iterable)
> 
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과를 map object로 반환
- 리스트 형 변환을 통해 결과 직접 확인

### filter

> filter(function, iterable)
> 
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과가 True인 것들을 filter object로 반환
- 리스트 형 변환을 통해 결과 직접 확인

### zip

> zip(*iterables)
> 
- 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
- 리스트 형 변환을 통해 결과 직접 확인

### lambda 함수

> lambda [parameter] : 표현식
> 
- 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수(익명 함수)
- 특징
    - return 문을 가질 수 없음
    - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 장점
    - 함수를 정의해서 사용하는 것보다 간결
    - def를 사용할 수 없는 곳에 사용 가능
    

### 재귀 함수(recursive function)

- 자기 자신을 호출하는 함수
- 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
    - 알고리즘 중 재귀 함수로 로직을 표현하기 쉬운 경우가 있음(예 - 점화식)
    - 변수의 사용이 줄어들며 코드의 가독성이 높아짐
- 1개 이상의 **base case(종료되는 상황)**가 존재하고, 수렴하도록 작성

### 재귀 함수 주의 사항

- 재귀 함수는 base case에 도달할 때까지 함수를 호출
- 메모리 스택이 넘치게 되면(stack overflow)프로그램이 동작하지 않게 됨
- 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1000번으로 정해져 있음(조정 가능)
    - 호출 횟수가 이를 넘어가게 되면 Recursion Error 발생

### 재귀 함수 사용 용도

- 알고리즘 자체가 재귀적인 표현이 자연스러운 경우
- 재귀 호출은 변수 사용을 줄여줄 수 있음
- 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림