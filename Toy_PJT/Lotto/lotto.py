# 여기에 필요한 모듈을 추가합니다.
import random
import json
import datetime


class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for _ in range(n):
            lotto_line = (random.sample(range(1, 46), 6))
            # 삼항 연산자 + 리스트 컴프리헨션 
            '''
            lotto_line = []
            while len(lotto_line) != 6:
                num = random.randint(1, 46)
                if num in lotto_line:
                    continue
                lotto_line.append(num)'''
            self.number_lines.append(sorted(lotto_line))


    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        year, month, day = self.get_draw_date(draw_number)
        drwno_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        drwno = json.load(drwno_json)
        days = ['월', '화', '수', '목', '금', '토', '일']
        print('=========================================')
        print(f'              제 {drwno["drwNo"]} 회 로또')
        print('=========================================')
        print(f'추첨일 : {year}/{month}/{day} ({days[datetime.date(int(year), int(month), int(day)).weekday()]})')
        print('=========================================')
        for line in range(len(self.number_lines)):
            print(f'{chr(65+line)} : {self.number_lines[line]}')
    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        main_numbers, bonus_number = self.get_lotto_numbers(draw_number)
        print('=========================================')
        print(f'당첨 번호 : {main_numbers} + {bonus_number}')
        print('=========================================')
        for line in range(len(self.number_lines)):
            same_main_counts, is_bonus = self.get_same_info(main_numbers, bonus_number, self.number_lines[line])
            ranking = self.get_ranking(same_main_counts, is_bonus)
            print(f'{chr(65+line)} : {str(same_main_counts)+"개 일치" if is_bonus == False else str(same_main_counts)+"개 + 보너스 일치"} ({"낙첨" if ranking == -1 else str(ranking)+"등 당첨!"})')
        return ranking
    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        drwno_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        drwno = json.load(drwno_json)
        date = drwno["drwNoDate"]
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        drwno_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        drwno = json.load(drwno_json)
        main_numbers = sorted([drwno[f'drwtNo{i}'] for i in range(1, 7)])
        bonus_number = drwno['bnusNo']
        return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts = 0
        is_bonus = False
        for num in line:
            if num in main_numbers:
                same_main_counts += 1
        if bonus_number in line:
            is_bonus = True
        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        ranks = [6, 5, 5, 4, 3]
        rank_no = 0
        for rank in range(len(ranks)):
            if ranks[rank] == same_main_counts:
                rank_no = rank + 1
                if rank_no == 2:
                    if is_bonus == False:
                        rank_no += 1
                break
        else:
            rank_no = -1

        return rank_no
