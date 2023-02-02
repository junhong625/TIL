import requests
import pprint

#### 프레시밀 (광주캠퍼스) 식단표

url = 'https://front.cjfreshmeal.co.kr/meal/v1/week-meal?storeIdx=6442&weekType=1'

res = requests.get(url)

# 월, 화, 수, 목, 금
week = ['mo','tu','we','th','fr']

# 식단 데이터
res = res.json()
data = res['data']

## 점심 관련 주요 정보
# res['data'] : 1주일 간의 식사 데이터  
# res['data'][day]['2'] : 점심 데이터 리스트
# res['data'][day]['2'][idx]['name'] : 점심 주메뉴 이름
# res['data'][day]['2'][idx]['side'] : 점심 사이드메뉴 이름
# res['data'][day]['2'][idx]['kcal'] : 점심 메뉴 칼로리
# res['data'][day]['2'][idx]['carb'] : 점심 메뉴 칼로리
# res['data'][day]['2'][idx]['protein'] : 점심 메뉴 칼로리
# res['data'][day]['2'][idx]['fat'] : 점심 메뉴 칼로리
# res['data'][day]['2'][idx]['salt'] : 점심 메뉴 칼로리
for day in week:
    menus = data[day]["2"]
    print(day)
    # pprint.pprint(menus)
    for menu in menus:
        course = menu['corner']
        main_menu = menu['name']
        sub_menu = menu['side']
        kcal = int(menu['kcal'])
        cho = int(menu['carb'])
        protein = int(menu['protein'])
        fat = int(menu['fat'])
        sodium = int(menu['salt'])
        image_url = menu['thumbnailUrl']
        print(f"코스 : {course}")
        print(f"주메뉴 : {main_menu}")
        print(f"사이드메뉴 : {sub_menu}")
        print(f"칼로리 : {kcal}")
        print(f"성분표 : [나트륨 : {sodium}mg , 탄수화물 : {cho}g, 지방 : {fat}g, 단백질 : {protein}g]")
        print(f"사진 : {image_url}")
        print()
    # print()