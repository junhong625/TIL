count = int(input())
switch_list = list(map(int, input().split()))
students = int(input())

for i in range(students):
    s, num = map(int,input().split())

    # 남학생일 경우
    if s == 1:
        # 주어진 스위치 번호(num)의 배수일 경우 값 변경
        for j in range(count):
            if (j+1) % num == 0:
                switch_list[j] = (switch_list[j] + 1) % 2
    
    # 여학생일 경우
    else:
        # 최대로 계산할 수 있는 대칭 범위
        max_width = min(count-num, num-1)
        # 주어진 스위치 번호(num)의 값 변경
        switch_list[num-1] = (switch_list[num-1] + 1) % 2
    
            # 주어진 스위치 번호(num)부터 대칭 값 비교하여 같을 경우 변경
        for j in range(1, max_width+1):
            if switch_list[num+j-1] == switch_list[num-j-1]:
                switch_list[num+j-1] = (switch_list[num+j-1] + 1) % 2
                switch_list[num-j-1] = (switch_list[num-j-1] + 1) % 2
            else:
                break

# 20번째 출력마다 개행
for i in range(count):
    print(switch_list[i], end=' ') if (i+1) % 20 != 0 else print(switch_list[i])