# Algorithm_4💡

# 스택

## 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 선형 구조를 가진 자료구조
    - 선형 구조 : 자료 간의 관계가 1대1의 관계
    - 비선형 구조 : 자료 간의 관계가 1대N의 관계
    - 그래프 구조 : 자료 간의 관계가 N대N의 관계
        
        > 비선형 구조인 그래프 구조는 그래프로 모든 자료를 빠짐없이 검색하는 것이 중요
        > 
- LIFO(Last-In First-Out)이라고 부른다.
- 스택에서 마지막 삽입된 원소의 위치 → TOP

## 연산

- 삽입 : 저장소에 자료를 저장, push
- 삭제 : 저장소에서 자료를 역순으로 꺼낸다, pop
- 공백인지 확인 : isEmpty(Bool타입 반환)
- top에 있는 원소(item)를 반환 : peek

## 구조

### push

```python
def push(item, size):
		global top
		top += 1
		if top == size:
				print('overflow')
		else:
				stack[top] = item
size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1         # push(20)
stack[top] = 20 
```

### pop

```python
def pop():
		global top
		if top == -1:
				print('underflow')
				return 0
		else:
				top -= 1
				return stack[top+1]
print(pop())

if top > -1:     # pop()
		top -= 1
		print(stack[top+1])
```