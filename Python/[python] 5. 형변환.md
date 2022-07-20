# 형 변환(Typecasting)

## 형변환이란

- 파이썬에서 데이터 형태는 서로 변환할 수 있음
- 암시적 형 변환(Implicit) → 파이썬(자동)
  - 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우
- 명시적 형 변환(Explicit) → 개발자(수동)
  - 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우

### 암시적 형 변환

- 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환 하는 경우
  
  - bool
  - Numeric type(`int`, `float`)
  
  ```python
  print(True + 3) # 4
  print(3 + 5.0) # 8.0
  ```
  

### 명시적 형 변환

- int
  
  - `str`, `float` ⇒ `int`
  - 단, 형식에 맞는 문자열만 정수로 변환 가능
  
  ```python
  # 문자열은 암시적 타입 변환이 되지 않음
  print('3' + 4) # TypeError: can only concatenate str(not "int") to str
  
  # 명시적 타입 변환이 필요함
  print(int('3') + 4) # 7
  
  # 정수 형식이 아닌 경우 타입 변환할 수 없음
  print(int('3.5') + 5) # ValueError: invalid literal for int() with base 10:
  ```
  
- float
  
  - `str`(참고), `int` ⇒ `float`
  - 단, 형식에 맞는 문자열만 `float`로 변환 가능
  
  ```python
  print('3.5' + 3.5) # TypeError: can only concatenate str(not "float") to str
  
  # 정수 형식인 경우에도 float로 타입 변환
  print(float('3')) # 3.0
  
  # float 형식이 아닌 경우 타입 변환할 수 없음
  print(float('3/4') + 5.3) # ValueError: could not convert string to float:
  ```
  

> `int`는 `float` 타입으로 항상 변환 가능

- str
  
  - `int`, `float`, `list`, `tuple`, `dict` ⇒ `str`
  
  ```python
  print(str(1)) # 1
  
  print(str(1.0)) # 1.0
  
  print(str([1, 2, 3])) # [1, 2, 3]
  
  print(str((1, 2, 3))) # (1, 2, 3)
  
  print(str({1, 2, 3})) # {1, 2, 3}
  ```
  

### 컨테이너 형 변환

- 컨테이너 간의 형 변환은 아래와 같이 가능
![](https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png)
---

# 프로그램 구성 단위

- 식별자(identifier)
  - 변수, 함수, 클래스 등 프로그램이 실행되는 동안 다양한 값을 가질 수 있는 이름
  - 예약어
    - 파이썬 키워드 (명령어)
- 리터럴(literal)
  - 읽혀지는 대로 쓰여있는 값 그 자체

### 프로그램 구성 단위

- 표현식(Expression)
  - 새로운 데이터 값을 생성하거나 계산하는 코드 조각
- 문장(Statement)
  - 특정한 작업을 수행하는 코드 전체
  - 파이썬이 실행 가능한 최소한의 코드 단위
  - 표현식은 값을 생성하는 일부분이고, 문장은 특정 작업을 수행하는 코드 전체

> **모든 표현식(expression)은 문장(statement)이다.**