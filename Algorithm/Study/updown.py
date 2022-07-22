import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    player_answer = 0
    while player_answer != answer:
        player_answer = int(input('1이상 10000이하의 숫자를 입력하세요. : '))
        if player_answer not in list(range(1, 10001)):
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.\n')
            continue
        if player_answer > answer:
            counts += 1
            print('Down!!!\n')
            continue
        elif player_answer < answer:
            counts += 1
            print('Up!!!\n')
            continue
        else:
            counts += 1
            print(f'Correct!!! {counts}회 만에 정답을 맞히셨습니다.\n')
            break
    more_play = input('게임을 재시작하시려면 y, 종료하시려면 n을 입력하세요.: ')
    if more_play == 'y':
        pass
    elif more_play == 'n':
        is_playing = False
        print('이용해주셔서 감사합니다.', end=' ')
    else:
        is_playing = False
        print('잘못된 값을 입력하셨습니다.', end=' ')
print('게임을 종료합니다.')    
