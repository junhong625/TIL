dice_cnt = int(input())
dice_list = [list(map(int, input().split())) for cnt in range(dice_cnt)]
total_list = []

# 주사위 맞은 편의 인덱스 값
pair_dict = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

# 제일 처음으로 나오는 아랫면을 1부터 6까지 돌아가면서 실행
for i in range(1, 7):
    # 아랫면 값
    bot_num = i
    # 주사위 수 * 6(최대값)
    total = dice_cnt * 6
    # 주사위를 하나씩 꺼내는 반복문
    for dice in dice_list:
        # 윗면 값
        top_num = dice[pair_dict[dice.index(bot_num)]]
        # 최소값이 5라는 것은 현재 윗면과 아랫면의 수가 5와6이라는 의미
        # 즉, 옆면에 있는 수들의 최대값은 4라는 의미
        # 그렇기에 total에서 2를 빼줌
        if 5 == min(bot_num, top_num):
            total -= 2
        # 위 조건식에 해당되지 않기에 6과 5가 동시에 존재할리가 없음 
        # 즉, 윗면과 아랫면에 6이 존재한다면 최대값은 5라는 의미
        # 그렇기에 total에서 1을 빼줌
        elif 6 in (bot_num, top_num):
            total -= 1
        else:
            pass
        bot_num = top_num
    total_list.append(total)
print(max(total_list))