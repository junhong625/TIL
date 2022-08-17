# Algorithm_5💡

# Memoization

> 컴퓨터 프로그램을 실행 시 이전에 계산한 값을 메모리에 저장하여 다시 계산하지 않도록 하여 전체적인 실행 속도를 높이는 기술
> 
- 동적 계획법의 핵심 기술
- Memoization을 활용한 피보나치 수를 구하는 식

```python
# momo를 위한 배열을 할당, 모두 0으로 초기화
# memo[0]을 0으로 memo[1]을 1로 초기화

def fibo1(n):
		global memo
		if n >= 2 and len(memo) <= n:
				memo.append(fibo1(n-1) + fibo1(n-2))
		return memo[n]

memo = [0, 1]
```

# DP(Dynamic Programming)

> 동적 계획 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다.
> 
- 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

### 구현 방식

- recursive 방식 : 위 memoization
- iterative 방식
    
    ```python
    def fibo(n):
        f = [0, 1]
    
        for i in range(2, n+1):
            f.append(f[i-1] + f[i-2])
            print(f'{i} : {f[i]}')
        return f[n]
    
    fibo(1000)
    ```
    

- memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현하는 것이 성능 면에서 보다 효율적
    - 재귀적 구조는 내부에 시스템 호출 스택을 사용하여 오버헤드가 발생하기 때문(함수 호출을 많이 하는 구조는 피하는 것이 필요)
    - 하지만 반드시 DP가 더욱 빠른 것은 아님