N = int(input())

# N만큼 반복하는 반복문
for num in range(1, N+1):
    count = 0
    # 3, 6, 9가 있는 자리 수만큼 count를 추가하여 출력해야할 -의 개수를 파악하는 반복문 
    for n in str(num):
        if n in ['3', '6', '9']:
            count += 1
    if count == 0:
        print(num, end='')
    else:
        print(count*'-', end='')
    print(' ', end='')