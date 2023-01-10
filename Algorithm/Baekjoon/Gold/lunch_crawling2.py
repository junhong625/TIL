import requests

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
for day in week:
    lunch = data[day]["2"]
    print(day)
    for i in range(len(lunch)):
        print(f"주메뉴 : {lunch[i]['name']}")
        print(f"사이드메뉴 : {lunch[i]['side']}")
        print(f"칼로리 : {lunch[i]['kcal']}kcal")
        print()
    print()