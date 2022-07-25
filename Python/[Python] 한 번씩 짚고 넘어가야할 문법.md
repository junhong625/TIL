# Python 🖥️

# Python 문법

## 인덴트(Indent)
> 파이썬의 대표적인 특징으로 공백 4칸을 원칙으로 한다.

### 예시
```python
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```
> 첫 번째 줄에 파라미터가 있다면 파라미터가 시작되는 부분에 맞춰 정렬

```python
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```
> 첫 번째 줄에 파라미터가 없다면, 공백 4칸 `인덴트`를 한 번 더 추가하여 다른 행과 구분

```python
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```
> 여러 줄로 나눠쓸 경우 다음 행과 구분 되도록 `인덴트`를 추가
<br>

## 네이밍 컨벤션(Naming Convention)
> 파이썬의 `네이밍 컨벤션`은 자바와 달리 밑줄`-`로 구분하여 표기하는 스네이크 케이스를 따른다.
- 파이썬의 PEP 8 및 철학에 따라 스네이크 코딩을 지향

### 예시
```python
# 스네이크 케이스
snake_case = 1
# 카멜 케이스
camelCase = 1
```
<br>

## 타입 힌트(Type Hint)
> 타입을 지정할 수 있는 `타입 힌트`를 통해 가독성을 높이고 버그 유발을 피할 수 있다.

### 예시
```python
# 변수 지정
a : str = "1"
b : int = 1

# 함수 생성
# parpameter a의 타입은 int
# return은 True or False여야 한다는 의미
def fn(a: int) -> bool:
    ...
```
> 하지만 실제로 강제 규약이 아니기 때문에 주의가 필요하다.
<br>

## 리스트 컴프리헨션(List Comprehension)
> 파이썬은 `map`, `filter`와 같은 함수형 기능을 지원하며 람다 표현식도 지원한다.

### 예시
```python
# 홀수인 경우 2를 곱해 출력하는 리스트 컴프리헨션 
odd = [n * 2 for in range(1, 11) if n % 2 == 1]

# 위 코드를 리스트 컴프리헨션을 사용하지 않은 경우
odd = []
for n in range(1, 11):
    if n % 2 == 1:
        odd.append(n * 2)
```
> 위와 같이 리스트 컴프리헨션을 사용할 경우 코드를 더욱 간결하게 작성할 수 있다.
> 하지만 무리해서 복잡하게 작성할 경우 가독성이 떨어뜨릴 수 있으므로 적절한 사용이 필요하다.

```python
# 딕셔너리 컴프리헨션
dictionary = {key : value for key, value in this.items()}
```
> 위와 같이 딕셔너리도 가능하다.
<br>

## 제너레이터(Generator)
> iterator를 생성해주는 함수, 함수안에 yield 키워드를 사용함
> 루프의 반복 동작을 제어할 수 있는 루틴 형태(간단하게 번역하자면 `yield` : 중간 저장 `next()` : 중간 저장한 값을 불러옴)
> 여러 타입의 값을 하나의 함수에서 생성도 가능

**의문점 한 가지** : 리스트가 아닌 굳이 제너레이터를 사용하는 이유?
- 리스트는 데이터를 한 번에 메모리에 적재하기에 메모리 부족현상이 발생해 프로그램이 죽을 수 있지만 제너레이터는 **데이터에 접근할 때마다 메모리에 적재**하기 때문에 리스트보다 **안정적이고 효율적**
- 리스트의 경우 `List Comprehension`을 수행할 때 리스트의 모든 값을 먼저 수행하기 때문에 연산이 오래 걸리거나 연산된 값에 접근하는 시간이 오래 걸리지만, `제네레이터`는 필요한 때에 `yield`를 통해 값에 접근하기 때문에 수행시간이 긴 연산을 필요한 순간까지 늦출 수 있음
- 그리고 `List`, `Set`, `Dictionary`의 표현식의 내부도 사실 `Generator`이다.
```python
type(x*x for x in range(3))
>> <class 'generator'> 
```

### 예시
```python
def get_num():
    for i in range(1, 11):
        yield i

numbers = get_num()
print(next(numbers))
print(next(numbers))
print(next(numbers))
...

>> 1
>> 2
>> 3
...
```
<br>

## range
> 제너레이터의 방식을 활용하는 대표적인 함수 
> 주로 for문에서 쓰인다.

### 예시
```python
list(range(5))
>> [1, 2, 3, 4, 5]
range(5)
>> range(0, 5)
for i in range(5):
    print(i, end=' ')
>> 0 1 2 3 4
```

### 주의할 점
> `range(1000000)`와 `[n for n in range(1000000)]`의 메모리 점유율 차이는 극명하다.
```python
a = range(1000000)
b = [n for n in range(1000000)]

len(a)
>> 1000000
len(b)
>> 1000000
```
> 위와 같이 a와 b의 길이는 같다. 그렇다면 메모리 점유율은??
```python
sys.getsizeof(a)
>> 48 
sys.getsizeof(b)
>> 8697464
```
> 이와 같이 엄청난 차이를 보인다.
> 그 이유는 바로 a는 생성해야 한다는 조건이 담겨있는 것이고 b는 이미 생성된 값들이 담겨있기 때문이다.
<br>

## enumerate
> `enumerate`는 '열거하다'는 뜻의 함수로 여러가지 자료형을 인덱스를 포함한 `enumerate` 객체로 리턴한다.

### 예시
```python
a = list(range(1, 6))
>> [1, 2, 3, 4, 5]
enumerate(a)
>> <enumerate object at 0x0000014D187F1AC0>
list(enumerate(a))
>> [(0,1), (1,2), (2,3), (3,4), (4,5)]
for idx, num in enumerate(a):
    print((idx, num), end=' ')
>> (0, 1) (1, 2) (2, 3) (3, 4) (4, 5)
```
> 이처럼 인덱스를 자동으로 부여해주기에 매우 편리하게 활용가능하다.
<br>

## locals
> `locals()`는 로컬에 선언된 모든 변수를 조회할 수 있는 명령어로 디버깅에 많은 도움이 된다.
> 특히 함수, 메소드 내부에서의 로컬 정보를 조회해 잘못 선언한 부분이 없는지 확인하는 용도로 활용할 수 있다.
> pprint를 함께 사용하여 출력하게 되면 가독성을 더욱 높여 디버깅을 할 수 있다.