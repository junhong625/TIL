# Python 🖥️

# 정리 및 요약

## 프로그래밍 기초
**변수** 
- 데이터를 언제든 할당할 수 있기 때문에 `변수`라고 불림
- 변수의 추상화
    - 코드의 가독성 증가
    - 코드 수정이 용이

**식별자**
- 영문 알파벳, 언더스코어(`-`), 숫자로 구성
- 첫 글자에 숫자 X
- 길이 제한 X, 대소문자 구별
- 예약어 사용 불가

---

## 자료형 분류
> `수치형`, `문자형`, `불린형`, `None`

**실수 연산 시**
- 부동 소수점으로 인해 실수 처리 값이 원하지 않은 값이 나올 수 있음
- `math`모듈의 `isclose()`함수 활용

**삼중 따옴표**
- 여러 줄 주석 처리
- 여러 줄을 나눠 입력할 때 편리

**Escape Sequence**
- 역슬래시와 특정 문자 조합으로 특수한 기능 수행
| 예약 문자 | 내용(의미) |
| --- | --- |
| \n  | 줄 바꿈 |
| \t  | 탭   |
| \r  | 캐리지 리턴 |
| \0  | 널(Null) |
| \\  | \   |
| \’  | 단일인용부호(’) |
| \”  | 이중인용부호(”) |

**String Interpolation**
- %-formatting
- str.format()
- f-string : python 3.6+

| %s  | 문자형 |
| --- | --- |
| %d  | 숫자형 |
| %f  | 실수형 |

**논리 연산자 단축 평가**
- 결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값 반환
- `and` 연산에서 첫번째 값이 `False`인 경우 무조건 `False` ⇒ 첫번째 값 반환
- `or` 연산에서 첫번째 값이 `True`인 경우 무조건 `True` ⇒ 첫번째 값 반환
- 0은 `False`, 1은 `True`
- **Falsy가 아닌 값들은 모두 `True`**
    - `False`, `null`, `undefined`, `0`, ``NaN``, `''`
- 비어있는 값들과 0은 `False`, 나머지는 `True`

---

## 컨테이너
### 시퀀스형, 비시퀀스형

**시퀀스형**
> 순서가 있는 데이터(iterable)
- List(가변형)
- Tuple(불변형)
- Range(불변형)

**비시퀀스형**
> 순서가 없는 데이터(non-iterable)
- set(가변형)
- dictionary(가변형)

### 가변, 불변 자료형
**가변형**
> 객체 생성 이후 값 변경 가능
- List, Set, Dictionary

**불변형**
> 객체 생성 이후 값 변경 불가
- Tuple, str, int, float, range, bool

**iterable**
- 순회할 수 있는 자료형(string, list, dict, tuple, range, set등)
- 순회형 함수(range, enumerate)

---

## 형변환
**암시적 형 변환**
- `bool`
- Numeric Type(`int`, `float`)

**명시적 형 변환**
- `int` -> `str`, `float`
- `float` -> `str`, `int`
- `str` -> `int`(정수형), `float`(실수형)

---

## 제어문
### 조건문, 반복문

**조건 표현식(삼항 연산자)**
```python
```true인 경우``` if 조건 else ```false인 경우```
```

**복합 연산자**
- 연산과 할당을 합쳐 놓은 것
- ex)
    ```python
    x += y # x = x + y
    ```

**List comprehension**
```python
[code for 변수 in iterable (if 조건식)]
```

---

## 함수
**분해**
> **기능을 분해하고 재사용 가능하게 만듦**

**추상화**
> **복잡한 내용을 모르더라도 사용할 수 있도록 재사용성과 가독성, 생산성 UP**

**함수 종류**
- Void function
    - return X
    - None을 반환
- Value returning function
    - return O

### Parameter
- 함수를 **정의할 때** 함수 내부에서 사용되는 변수

### Argument
- 함수를 **호출할 때** 넣어주는 값

**Positional Arguments**
- 위치에 맞춰 함수 내에 전달

**Keyword Arguments**
- 직접 변수의 이름으로 특정 `Argument`를 전달
- Keyword Arguments다음으로 Positional Arguments 사용 X

**Defualt Arguments**
- 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함

**가변인자 `(*args)`**
- 애스터리스크(Asterisk) 혹은 언패킹 연산자인 `*` 사용
- 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
- 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용

**가변 키워드 인자(**kwargs)**
- 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
- `**kwargs`는 **딕셔너리로 묶여 처리**되며, `parameter`에 `**`를 붙여 표현
