# Algorithm_8💡

# 큐(Queue)

> 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 선형 자료구조
> 
- 큐의 앞: 삭제만 가능 / 큐의 뒤: 삽입만 가능
- 선입선출(FIFO : First-In First-Out)구조

## 큐의 주요 연산

| 연산 | 기능 |
| --- | --- |
| enQueue(item) | 큐의 뒤쪽(rear)에 원소를 삽입 |
| deQueue() | 큐의 앞쪽(front)에 원소를 삭제하고 반환 |
| createQueue() | 공백 상태의 큐를 생성 |
| isEmpty() | 큐가 공백 상태인지 확인 |
| isFull() | 큐가 포화 상태인지 확인 |
| Qpeek() | 큐의 앞쪽(front)에서 원소를 삭제 없이 반환 |

## 선형 큐

> 1차원 배열을 이용한 큐
> 
- front: 저장된 첫 번째 원소의 인덱스
- rear: 저장된 마지막 원소의 인덱스

### 기본 연산 과정

- 초기 공백 상태
    - front = rear = -1
- 삽입
    - rear + 1
- 삭제
    - front + 1
- 공백 상태
    - front == rear
- 포화 상태
    - rear == n-1
    
    ### enQueue 구현
    
    ```python
    Q = []
    
    def enQueue(item):
    		global rear
    		if isFull() : print("Queue_Full")
    		else:
    				rear += 1
    				Q[rear] = item
    ```
    
    ### deQueue 구현
    
    ```python
    def deQueue():
    		if isEmpty() : print("Queue_Empty")
    		else:
    				front += 1
    				return Q[front] 
    ```
    

## 원형 큐

> 배열의 끝과 배열의 처음이 연결된 큐
> 
- 초기 공백 상태 → front = rear = 0
    
    ### enQueue 구현
    
    ```python
    Q = []
    
    def enQueue(item):
    		global rear
    		if isFull() : print("Queue_Full")
    		else:
    				rear = (reat + 1) % len(Q)
    				Q[rear] = item
    ```
    
    ### deQueue 구현
    
    ```python
    def deQueue():
    		if isEmpty() : print("Queue_Empty")
    		else:
    				front = (front + 1) % len(Q)
    				return Q[front] 
    ```
    

|  | 삽입 위치 | 삭제 위치 |
| --- | --- | --- |
| 선형큐 | rear = rear + 1 | front = front + 1 |
| 원형큐 | rear = (rear+1) mod n | front = (front+1) mod n |

# 우선순위 큐(Priority Queue)

> 우선순위를 가진 항목들을 저장하는 큐
> 

## 특성

- FIFO 구조가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.

### 적용 분야

- 시뮬레이션 시스템
- 네트워크 트래픽 제어
- 운영체제의 테스크 스케줄링

# 버퍼(Buffer) → 큐의 활용

> 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
> 

## 특성

- 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미한다.
- 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용
- 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐를 활용