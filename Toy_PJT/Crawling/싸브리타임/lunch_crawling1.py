import requests
import pprint
import datetime

#### welstory 식단표

## 식단 날짜
# 년원일 형식
date = datetime.date(2023, 2, 14)
week = datetime.datetime.weekday(date)
while week:
    date = date - datetime.timedelta(days=1)
    week = datetime.datetime.weekday(date)

date = str(date).split()[0].replace("-", "")
print(date)
## restaurantCode 분류
# 서울 : REST000133
# 부울경 : REST000595
# 구미 : REST000213
restaurantCode = 'REST000133'

## hallNo 분류
# 서울 : E110
# 부울경 : E32M
# 구미 : E21F
hallNo = "E110"

## menuCourseType 분류
# 서울 : ["BB", "CC"] 
# 부울경 : ["AA", "BB", "CC", "DD", "EE", "JK", "ZZ", "JJ", "KK", "MM", "NN", "OO", "PP", "RR", "SS", "T2", "T3", "WF"]
# 구미 : ["AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II" , "JJ", "KK", "LL", "MM", "NN", "OO"]

url = f"https://welplus.welstory.com/api/meal/detail?menuDt={date}&hallNo=E110&menuCourseType=BB&menuMealType=2&restaurantCode={restaurantCode}"

## 인증 쿠키
# remember-me : 회원정보 세션 
cookies = {
    'remember-me':'anVuaG9uZzYyNToyNjE5MzkyNTc2NTM2OjJmZGMyMzEyY2MyN2FmMDU2ZjU0YjRmOGNkZTMwMjRk',
}

## 점심 관련 주요 정보
# res['data'] : 점심 메뉴 리스트
# res['data']['subMenuTxt'] : 메뉴
# res['data']['sumKcal'] : 칼로리
# res['data']['totCho'] : 탄수화물
# res['data']['totNa'] : 나트륨
# res['data']['totFat'] : 지방
# res['data']['totProtein'] : 단백질
res = requests.get(url, cookies=cookies).json()
# pprint.pprint(res)
main_menu, sub_menu = "", ""
kcal, cho, protein, fat = 0, 0, 0, 0
image_url = ""
for idx, menu in enumerate(res['data']):
    if idx == 0:
        image_url = menu['photoUrl']+menu['photoCd'] if menu['photoUrl'] and menu['photoCd'] else ""
        main_menu = menu['menuName']
    else: 
        sub_menu += f", {menu['menuName']}" if sub_menu else menu['menuName']
    if not kcal:
        kcal = menu['sumKcal']
        cho = menu['totCho']
        protein = menu['totProtein']
        fat = menu['totFat']
        sodium = menu['totNa']

print(f"메인 메뉴 : {main_menu}")
print(f"서브 메뉴 : {sub_menu}")
print(f"칼로리 : {kcal}kcal")
print(f"성분표 : [탄수화물 : {cho}g, 나트륨 : {sodium}mg , 지방 : {fat}g, 단백질 : {protein}g]")
print(f"사진 : {image_url}")
print()