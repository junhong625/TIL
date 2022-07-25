# Python_10 🖥️

# 데이터 구조

## 데이터 구조 활용

- 데이터 구조를 활용하기 위해서는 메서드(method)를 활용
    - 메서드는 클래스 내부에 정의한 함수, 사실상 함수 동일
    - 쉽게 설명하자면 객체의 **기능**(추후 객체 지향 프로그래밍에서 학습

> **`데이터 구조**.**메서드()**` 형태로 활용
> 

### 파이썬 공식 문서의 표기법

- python 구문이 아니며, 문법을 표현하기 위한 것임
- 아래 예시에서 `str.replace(old, new[,count])`
    - `old`, `new`는 필수 `[,count]`는 선택적 인자를 의미

---

# 순서가 있는 데이터 구조

## 문자열(String Type)

- 문자들의 나열(sequence of characters)
    - 모든 문자는 str타입(변경 불가능한 immutable)
- 문자열은 작은 따옴표 `’` 나 큰 따옴표 `”` 를 활용하여 표기
    - 문자열을 묶을 때 동일한 문장 부호를 사용
    - PEP8에서는 소스 코드 내에서 하나의 문장 부호를 선택하여 유지하도록 함

## 문자열 조회/탐색 및 검증 메서드

| 문법 | 설명 | 특징 |
| --- | --- | --- |
| s.find(x) | x의 첫 번째 위치를 반환. 없으면 -1을 반환  | 오류 X |
| s.index(x) | x의 첫 번째 위치를 반환. 없으면 오류 발생 | 오류 O |
| s.isalpha() | 문자 여부 | ≠ isdigit() |
| s.isupper() | 대문자 여부
* 단순 알파벳이 아닌 유니코드 상 Letter |  |
| s.islower() | 소문자 여부 |  |
| s.istitle() | 타이틀 형식 여부 |  |
| isdecimal() |  |  |
| isdigit() |  |  |
| isnumenric() |  |  |
- isdecimal() < isdigit() < isnumeric()

## 문자열 변경 메서드(S는 문자열)

| 문법 | 설명 |
| --- | --- |
| s.replace(old, new[,count]) | 바꿀 대상 글자를 새로운 글자로 바꿔서 전환 |
| s.strip([chars]) | 공백이나 특정 문자를 제거 |
| s.split(sep=None, maxsplit=-1) | 공백이나 특정 문자를 기준으로 분리 |
| ‘separator’.join([iterable]) | 구분자 iterable을 합침 |
| s.capitalize() | 가장 첫 번째 글자를 대문자로 변경 |
| s.title() | 문자열 내 띄어쓰기(+ 따옴표)기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환 |
| s.upper() | 모두 대문자로 변경 |
| s.lower() | 모두 소문자로 변경 |
| s.swapcase() | 대↔소문자 서로 변경 |

---

# 리스트

## 리스트의 생성과 접근

- 리스트는 대괄호 `[]` 혹은 list()를 통해 생성
    - 파이썬에서는 어떠한 자료형도 저장할 수 있으며, 리스트 안에 리스트도 넣을 수 있음
    - 생성된 이후 내용 변경이 가능 → 가변 자료형
    - 이러한 유연성 때문에 파이썬에서 가장 흔히 사용
- 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
    - 값에 대한 접근은 list[i]

## 리스트 메서드

| 문법 | 설명 | 특징 |
| --- | --- | --- |
| L.append(a) | 리스트 마지막에 a를 추가 |  |
| L.insert(a, b) | 리스트 인덱스 a에 b를 삽입 | a가 리스트 길이보다 큰 경우 맨 뒤에 삽입  |
| L.remove(a) | 리스트 가장 왼쪽에 있는 항목(첫 번째) a를 제거
항목이 존재하지 않을 경우, ValueError |  |
| L.pop() | 리스트 가장 오른쪽에 있는 항목을 반환 후 제거 |  |
| L.pop(a) | 인덱스 a의 값을 반환 후 제거 |  |
| L.extend(iterable) | iterable 의 모든 항목들의 리스트 끝에 추가 (+=과 같은 기능)  | 문자열을 argument로 넣을 시 문자로 하나하나 나눠서 삽입 |
| L.index(a, start, end) | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 a의 인덱스를 반환 |  |
| L.reverse() | 거꾸로 정렬 | None을 반환 |
| L.sort() | 정렬(매개 변수 이용 가능) | None을 반환 |
| L.count(x) | 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환 |  |
| L.clear() | 리스트의 값을 모두 삭제 |  |

## 탐색 및 정렬

### .sort()

- **원본** **리스트**를 정렬함.
- `None`을 반환

### .reverse()

- **원본 리스트**를 뒤집음
- `None`을 반환

---

# 튜플(Tuple)

- 튜플은 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
    - 리스트와의 차이점은 생성 후, 담고 있는 값 변경이 불가(불변 자료형)
- 소괄호 `()` 형태로 사용
- 튜플은 변경할 수 없기 때문에 값에 영향을 미치지 않는 메서드만을 지원

## 멤버십 연산자(Membership Operator)

- 멤버십 연산자 in을 통해 특정 요소가 속해 있는지 확인
    - in
    - not in

## 시퀀스형 연산자(Sequence Type Operator)

- 산술 연산자(+)
    - 시퀀스 간의 concatenation(연결/인쇄)
- 반복 연산자(*)
    - 시퀀스를 반복

---

# 비시퀀스형 데이터 구조

# 셋(Set)

- Set이란 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음
    - 데이터의 중복을 허용하지 않기 때문에 중복되는 원소가 있다면 하나만 저장
    - 순서가 없기 때문에 인덱스를 이용한 접근 불가
- 수학에서의 **집합**을 표현한 컨테이너
    - 집합 연산이 가능(여집합 연산자는 X)
    - 중복된 값이 존재하지 않음
- 담고 있는 요소를 삽입 변경, 삭제 가능 → 가변 자료형(mutable)

## 셋 메서드(s는 셋)

| 문법 | 설명 | 특징 |
| --- | --- | --- |
| s.copy() | 셋의 얕은 복사본을 반환 |  |
| s.add(x) | 항목 x가 셋 s에 없다면 추가 |  |
| s.update(t) | 셋 t에 있는 모든 항목 중 셋 s에 없는 항목을 추가 |  |
| s.pop() | 셋 s에서 랜덤하게 항복을 반환하고 제거
set이 비어있을 경우 KeyError |  |
| s.remove(s) | 항목 x를 셋 s에서 삭제
항목이 존재하지 않을 경우 KeyError | 에러 O |
| s.discard(x) | 항목 x가 셋 s에 있는 경우, 항목 x를 셋 s에서 삭제 | 에러 X |
| s.clear() | 모든 항목을 제거 |  |
| s.isdisjoint(t) | 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True반환 |  |
| s.issubset(t) | 셋 s가 셋 t의 하위 셋인 경우, True 반환 |  |
| s.issuperset(t) | 셋 s가 셋 t의 상위 셋인 경우, True 반환 |  |
- s.isdisjoing(t)
    - 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True 반환(서로소)
    - 교집합 X
- s.issubset(t)
    - 셋 s가 셋 t의 하위 셋인 경우, True반환
- s.issuperset(t)
    - 셋 s가 셋 t의 상위 셋인 경우, True반환

---

# 딕셔너리(Dictionary)

## 딕셔너리의 정의

- 키-값(key-value) 쌍으로 이뤄진 자료형(3.7버전 이후부터 ordered)
- Dictionary의 키(key)
    - key는 변경 불가능한 데이터(immutable)만 활용 가능
        - string, integer, float, boolean, tuple, range
- 각 키의 값(values)
    - 어떠한 형태든 상관없음

## 딕셔너리 메서드

| 문법 | 설명 |  |
| --- | --- | --- |
| d.clear() | 모든 항목을 제거 |  |
| d.copy() | 딕셔너리 d의 얕은 복사본을 반환 |  |
| d.keys() | 딕셔너리 d의 모든 키를 담은 뷰를 반환 |  |
| d.values() | 딕셔너리 d의 모든 값을 담은 뷰를 반환 |  |
| d.items() | 딕셔너리 d의 모든 키-값의 쌍을 담은 뷰를 반환 |  |
| d.get(k) | 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 None을 반환 |  |
| d.get(k, v) | 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 v을 반환 |  |
| d.pop(k) | 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제, 키 k가 딕셔너리 d에 없을 경우 KeyError를 발생 |  |
| d.pop(k, v) | 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제, 키 k가 딕셔너리 d에 없을 경우 v를 반환 |  |
| d.update([other]) | 딕셔너리 d의 값을 매핑하여 업데이트 | ex) d.update(key = 문자열) |

---

# 얕은 복사와 깊은 복사(Shallow Copy & Deep Copy)

## 할당(assignment)

- 대입 연산자 `=`
    - 리스트 복사 확인하기

## 얕은 복사

> 대입 연산 `=`를 통한 복사는 해당 객체에 대한 객체 참조를 복사
> 

```python
original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list)
# [1, 2, 3] [1, 2, 3]
copy_list[0] = 'hello'
print(original_list, copy_list)
# ['hello', 2, 3] ['hello', 2, 3]
```

### 해결법

> Slice 연산자 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사 (다른 주소)
> 

```python
original_list = [1, 2, 3]
copy_list = original_list[:]
print(a, b) 
# [1, 2, 3] [1, 2, 3]
b[0] = 5
print(a, b)
# [1, 2, 3] [5, 2, 3]
```

### 얕은 복사(shallow copy) 주의사항

> 복사하는 리스트의 **원소가 주소를 참조**하는 경우
> 

```python
a = [1, 2, [3, 4]]
b = a[:]
print(a, b)
# [1, 2, [3, 4]] [1, 2, [3, 4]]
b[2][0] = 0
print(a, b)
# [1, 2, [0, 4]] [1, 2, [0, 4]]
```

### 해결법

> `copy.deepcopy()`를 활용하기
```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
print(a, b)
# [[1, 2], [3, 4]] [[1, 2], [3, 4]]
b[0][1] = 8
print(a, b)
# [[1, 2], [3, 4]] [[1, 8], [3, 4]]
```