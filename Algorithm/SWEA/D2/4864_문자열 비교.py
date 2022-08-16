T = int(input())
for t in range(1, T+1):
	word = input()
	sentence = input()
	print(f'#{t}', end=' ')
	if word in sentence: # word가 sentence안에 존재하는지 확인
		print(1)
	else:
		print(0)