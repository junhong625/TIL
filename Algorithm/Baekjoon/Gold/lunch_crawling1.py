import requests

#### welstory 식단표

## 식단 날짜
# 년원일 형식
date = '20230110'

## restaurantCode 분류
# 서울 : REST000133
# 부울경 : REST000595
# 구미 : REST000213
restaurantCode = 'REST000595'

url = f"https://welplus.welstory.com/api/meal?menuDt={date}&menuMealType=2&restaurantCode={restaurantCode}"

## 인증 쿠키
# remember-me : 회원정보 세션 
cookies = {
    'remember-me':'anVuaG9uZzYyNToyNjE5MzkyNTc2NTM2OjJmZGMyMzEyY2MyN2FmMDU2ZjU0YjRmOGNkZTMwMjRk',
}

## 점심 관련 주요 정보
# res['data']['mealList'] : 점심 메뉴 리스트
# res['data']['mealList'][idx]['subMenuTxt'] : idx번 메뉴
# res['data']['mealList'][idx]['Kcal'] : idx번 메뉴 칼로리
# res['data']['mealList'][idx]['sumNa'] : idx번 메뉴 칼로리
# res['data']['mealList'][idx]['sumFat'] : idx번 메뉴 칼로리
# res['data']['mealList'][idx]['sumProtein'] : idx번 메뉴 칼로리
res = requests.get(url, cookies=cookies).json()
print(res)
# for menu in res['data']['mealList']:
#     print(f"메뉴 : {menu['subMenuTxt']}")
#     print(f"칼로리 : {menu['kcal']}kcal")
#     print(f"성분표 : [나트륨 : {menu['sumNa']}g , 지방 : {menu['sumFat']}g, 단백질 : {menu['sumProtein']}g]")
#     print()
