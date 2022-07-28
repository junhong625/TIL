from lotto import Lotto  # lotto.py에서 Lotto 클래스 import

draw_number = 1023  # 회차 번호(1023, 1024, 1025회차)
  # Lotto 클래스의 인스턴스 선언

# 1. 생성할 로또 번호의 줄 개수 입력받기
# 아래에 1번 요구사항을 만족하기 위한 코드를 추가합니다.
ranking = 0
count = 0
rank_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, -1: 0}
while ranking != 1:
    lotto = Lotto()
    n = 5
    '''
    n = 0
    while True:
        n = int(input('생성할 로또 줄 개수를 입력하세요.(1줄에서 5줄까지 생성 가능) : '))
        if n < 1 or n > 5:
            print(f'1줄에서 5줄 까지만 생성 가능합니다. 다시 입력하세요.\n')
            continue
        break
    '''
    # 아래 코드는 별도로 수정하지 않습니다.
    # 2. 로또 번호 생성하기
    lotto.generate_lines(n)

    # 3. 회차, 추첨일, 로또 번호 출력하기
    lotto.print_number_lines(draw_number)

    # 4. 당첨 번호와 당첨 결과 출력하기
    ranking = lotto.print_result(draw_number)
    count += 1
    rank_count[ranking] += 1
    print(ranking, count)
print(f'{count}회 만에 1등 당첨!!!!')
print(rank_count)