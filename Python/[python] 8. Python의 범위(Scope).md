# Python_8 🖥️

# Python의 범위(Scope)

- 함수는 코드 내부에 local scope를 생성하며, 그외의 공간인 global scope로 구분
- scope
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능
- variable
    - global variable(전역 변수) : global scope에 정의된 변수
    - local variable(지역 변수) : local scope에 정의된 변수
    - 가비지 콜렉션 ⇒ 지역 변수는 함수가 끝나며 메모리에서 사라짐

## 변수 수명 주기(lifecycle)

- 변수는 각자의 수명 주기(lifecycle)가 존재
    - built-in scope
        - 파이썬이 실행된 이후부터 영원히 유지
    - global scope
        - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    - local scope
        - 함수가 호출될 때 생성되고, 함수가 종료(`return`)될 때까지 유지
- 예시

```python
def func():
    a= 20
    print('local', a) 
func() # local 20
print('global', a) # NameError: name 'a' is not defined
```

## 이름 검색 규칙(Name Resolution)

- 파이썬에서 사용되는 이름(식별자)들은 이름 공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아나가며, **LEGB Rule**이라고 부름
    - **L**ocal scope : 지역 범위(현재 작업 중인 범위)
    - **E**nclosed scope : 지역 범위 한 단계 위 범위
    - **G**lobal scope : 최상단에 위치한 범위
    - **B**uilt-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)
        - ex) print()
- **함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음**
- 예시

```python
print(sum) # <built-in function sum> => LEG에 sum이 없기에 B에서 발견
print(sum(range(2))) # 1

sum = 5 # Global scope에 sum 생성
print(sum) # 5
print(sum(range(2))) # TypeError : 'int' object is not callable 
# => G에 sum이 있기에 B에 있는 sum내장 함수보다 먼저 탐색 됨 
```

### global 문

- 현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이 global variable임을 나타냄
    - `global`에 나열된 이름은 같은 코드 블록에서 `global` 앞에 등장할 수 없음
    - `global`에 나열된 이름은 `parameter`, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함

```python
# 함수 내부에서 글로벌 변수 변경하기
a = 10
def func1():
    global a
    a = 3

print(a) # 10
func1()
print(a) # 3
```

> Local scope에서 global 변수 값의 변경
> 

### nonlocal

- **global을 제외**하고 가장 가까운 (둘러싸고 있는) scope의 변수를 연결하도록 함
    - nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
    - nonlocal에 나열된 이름은 `parameter`, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
- global과는 달리 이미 존재하는 이름과의 연결만 가능함

```python
# nonlocal 예시
x = 0
def func1():
    x = 1
    def func2():
        nonlocal x
        x = 2
    func2()
    print(x) # 2

func1()
print(x) # 0 
```

### nonlocal, global 비교

- global - 존재하지 않는 변수도 사용 가능

```python
# 선언된 적 없는 변수의 활용
def func1():
    global out
    out = 3

func1()
print(out) # 3
```

- local - 존재하는 변수만 사용 가능

```python
# 선언된 적 없는 변수의 활용
def func1():
    def func2():
        nonlocal y
        y = 2
    func2()
    print(y)

func1()

# SyntaxError: no binding for nonlocal 'y' found
```

## 함수의 범위 주의

- 기본적으로 함수에서 선언된 변수는 Local scope에 생성되며, 함수 종료 시 사라짐
- 해당 scope에 변수가 없는 경우 LEGB rule에 의해 이름을 검색함
    - 변수에 접근은 가능하지만, 해당 변수를 수정할 수는 없음
    - 값을 할당하는 경우 해당 scope의 이름 공간에 새롭게 생성되기 때문
    - **단, 함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용할 것**
- 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능
    - 단, 코드가 복잡해지면서 변수의 변경을 추적하기 어렵고, 예기치 못한 오류가 발생 가능
    - 가급적 사용하지 않는 것을 권장, **함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 리턴 값을 사용하는 것을 추천**