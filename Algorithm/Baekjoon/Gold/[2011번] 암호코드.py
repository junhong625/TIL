import sys

input = sys.stdin.readline

code = input().rstrip()

## 궁금증(1)
# 여기서 dp를 생성할 때 값을 0이 아닌 1로 설정하여 dp를 생성해도 정답을 맞추는덴 문제가 없는데 왜 36ms가 더 늘어날까요?
dp = [0] * (len(code)+1) 														                              # code의 첫번째 자리 숫자부터 바로 판단을 할 수 있도록 padding처리
dp[0] = 1 																		                                    # 기준치 설정

code_length = len(code)															                              # code의 길이 변수로 저장
judge = False																	                                    # 현재 자리수의 앞자리 경우의 수가 2개였는지 확인(이를 통해 현재 자리수에서 어떤 연산을 할지 결정되기 때문)

# 이 코드를 넣냐 안 넣느냐에 따라 4ms차이
if not code:
    print(0)
    quit()

for i in range(code_length):
    if code[i] == '0' and (i == 0 or code[i-1] == '0' or code[i-1:i+1] > '26'): 	# 종료되야 하는 조건들
        print(0)
        quit()
    if code[i-1:i+1] > '26' or (i+1 < code_length and code[i+1] == '0')\
	      or code[i] == '0' or code[i-1:i+1] <= '10': 								              # 경우의 수가 1개인 조건들(줄바꿈으로 인해 4ms 증가)
        judge = False																					
        dp[i+1] = dp[i]																                            # 경우의 수가 1개인 경우 (앞자리 경우의 수 * 1)을 해주면 되기에 앞 자리 경우의 수를 그대로 할당
    else:																			                                    # 경우의 수가 2개인 조건들
        if judge:																	                                # 앞자리 경우의 수가 2개일 경우
            dp[i+1] = dp[i] + dp[i-1]									                            # 앞과 앞앞자리 경우의 수를 더해 현재 자리수에 할당
        else:																		                                  # 앞자리 경우의 수가 1개였을 경우
            dp[i+1] = dp[i] * 2												                            # (앞자리 경우의 수 * 2) 를 현재 자리수에 할당
            judge = True															                            # 경우의 수가 2개이기에 judge를 True로 변경

print(dp[-1] % 1000000)