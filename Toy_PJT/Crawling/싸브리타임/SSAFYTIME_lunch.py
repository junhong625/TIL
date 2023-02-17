from flask import Flask, request
import pymysql, requests, datetime, requests, pprint
from apscheduler.schedulers.background import BackgroundScheduler
from requests.auth import HTTPBasicAuth

app = Flask(__name__)


## get JIRA Issues(GET)
# name : 사용자 이름
# email : jira ID
# token : jira API Token 
@app.route("/jira/issue", methods=["GET"])
def get_issues():
    params = request.get_json()
    name = params['name']
    token = params['token']
    email = params['email']

    if request.method == "GET":
        jql = f"assignee={name} and status not in (closed, done)" # jql : 담당자가 name이고 상태(status)가 진행 중인 이슈 조회 

        url = f"https://ssafy.atlassian.net/rest/api/3/search"

        auth = HTTPBasicAuth(email, token)  # Basic인증 방식

        headers = {
        "Accept": "application/json"
        }

        query = {
        'jql' : jql
        }

        result = requests.get(url=url, headers=headers, params=query, auth=auth).json()
        issues = result['issues']
        issue_list = []

        # result['issues']['fields']['summary'] : issue name
        pprint.pprint(result)
        for issue in issues:
            issue_list.append(issue['fields']['summary'])

        return {'issue_list':issue_list}


## Insert lunch menu to ssaveryTime_DB
# DB 연결을 위한 기본 변수
# host      : ip 주소
# user      : DB 접속 ID
# password  : DB 접속 password
# db        : 연결할 DB 이름
# charset   : 문자 인코딩 방식 
host        = "i8a602.p.ssafy.io"
port        = 3306
user        = "root"
password    = "ssafy"
db          = "ssafy_web_db"
charset     = "utf8"

@app.route("/lunch_menu", methods=['GET'])
def lunch_menu_data():
    if request.method == 'GET':

        conn    = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
        cur     = conn.cursor()

        ## 인증 쿠키
        # remember-me : 회원정보 세션
        # 만료일 : 2024-02-14 T01:12:14.807Z
        cookies = {
            'remember-me':'anVuaG9uZzYyNToyNjE5MzkyNTc2NTM2OjJmZGMyMzEyY2MyN2FmMDU2ZjU0YjRmOGNkZTMwMjRk',
        }

        ## 식단 날짜
        # 년원일 형식
        date_data = datetime.date.today()
        date_data = date_data - datetime.timedelta(days=date_data.weekday()) # 이번주 월요일로 날짜 변경
        weekday = datetime.datetime.weekday(date_data)

        date = str(date_data).split()[0].replace("-", "")

        # 데이터를 수집하는 날짜는 매주 월요일
        # 월요일부터 금요일까지의 점심 데이터 수집
        while weekday <= 4:

        # ==================================================================================================================
        # Welstory+ 메뉴
        # ==================================================================================================================
            ## restaurantCode 분류
            # 서울 : REST000133
            # 부울경 : REST000595
            # 구미 : REST000213

            ## hallNo 분류
            # 서울 : E110
            # 부울경 : E32M
            # 구미 : E21F

            ## menuCourseType
            menuCourseType = {
            'E110' : ["BB", "CC"],
            'E32M' : ["BB", "CC", "DD", "AA", "EE"], 
            'E21F' : ["AA", "BB"]
            }
            for region, (restaurantCode, hallNo) in enumerate([('REST000133', 'E110'), ('REST000595', 'E32M'), ('REST000213', 'E21F')]):
                for mct in menuCourseType[hallNo]:
                    url = f"https://welplus.welstory.com/api/meal/detail?menuDt={date}&hallNo={hallNo}&menuCourseType={mct}&menuMealType=2&restaurantCode={restaurantCode}"
                    
                    # ==================================================================================================================
                    # 점심 관련 주요 정보
                    # res['data'] : 점심 메뉴
                    # res['data']['courseTxt'] : 코스
                    # res['data']['menuName'] : 메뉴 이름
                    # res['data']['sumKcal'] : 칼로리
                    # res['data']['totCho'] : 탄수화물
                    # res['data']['totNa'] : 나트륨
                    # res['data']['totFat'] : 지방
                    # res['data']['totProtein'] : 단백질
                    # res['data']['photoUrl'] + res['data']['photoCd'] : 이미지 URL
                    res = requests.get(url, cookies=cookies).json()
                    if not res['data']:
                        continue
                    main_menu, side_menu = "", ""
                    kcal, cho, protein, fat = 0, 0, 0, 0
                    image_url = ""
                    course = ""
                    for idx, menu in enumerate(res['data']):
                        if idx == 0:
                            image_url = menu['photoUrl']+menu['photoCd'] if menu['photoUrl'] and menu['photoCd'] else ""
                            main_menu = menu['menuName']
                            course = menu['courseTxt']
                        else: 
                            side_menu += f", {menu['menuName']}" if side_menu else menu['menuName']
                        if not kcal:
                            kcal = int(menu['sumKcal'].replace(",", ""))
                            cho = int(menu['totCho'].replace(",", ""))
                            protein = int(menu['totProtein'].replace(",", ""))
                            fat = int(menu['totFat'].replace(",", ""))
                            sodium = int(menu['totNa'].replace(",", ""))

                    # ==================================================================================================================
                    # 데이터 분류
                    # course    : 코스 (ex : 한식, 일식)
                    # main_menu : 메인 메뉴
                    # sub_menu  : 서브 메뉴
                    # kcal      : 메뉴 칼로리
                    # cho       : 메뉴 탄수화물
                    # fat       : 메뉴 지방
                    # protein   : 메뉴 단백질
                    # image_url : 메뉴 이미지 URL

                    # DB에 데이터 Insert
                    cur.execute(f"SELECT * FROM lunch_menu where date='{date}' and main_menu='{main_menu}' and side_menu='{side_menu}' and region='{region}'")
                    if (not cur.fetchall()):
                        cur.execute(f"INSERT INTO lunch_menu (date, region, course, main_menu, side_menu, kcal, cho, fat, protein, sodium, image_url) VALUES('{date}', '{region}', '{course}', '{main_menu}', '{side_menu}', '{kcal}', '{cho}', '{fat}', '{protein}', '{sodium}', '{image_url}')")
                    else:
                        return "Duplicate Data", 202

            date_data = date_data + datetime.timedelta(days=1)
            weekday = date_data.weekday()
            date = str(date_data).split()[0].replace("-", "")


        # ==================================================================================================================
        # Freshmeal 메뉴
        # 프레시밀 (광주캠퍼스) 식단표
        # ==================================================================================================================

        date_data = date_data - datetime.timedelta(days=6)
        region = 3

        ## 데이터 수집 날짜(월) - weekType=1
        ## 데이터 수집 날짜(토,일) - weekType=2
        weekType = 1

        url = f'https://front.cjfreshmeal.co.kr/meal/v1/week-meal?storeIdx=6442&weekType={weekType}'

        res = requests.get(url)

        # 월, 화, 수, 목, 금
        week = ['mo','tu','we','th','fr']

        # 식단 데이터
        res = res.json()
        data = res['data']
        # ==================================================================================================================
        # 점심 관련 주요 정보
        # res['data']                                   : 1주일 간의 식사 데이터  
        # res['data'][day]['2']                         : 점심 데이터 리스트
        # res['data'][day]['2'][idx]['name']            : 점심 주메뉴 이름
        # res['data'][day]['2'][idx]['side']            : 점심 사이드메뉴 이름
        # res['data'][day]['2'][idx]['kcal']            : 점심 메뉴 칼로리
        # res['data'][day]['2'][idx]['carb']            : 점심 메뉴 탄수화물
        # res['data'][day]['2'][idx]['protein']         : 점심 메뉴 단백질
        # res['data'][day]['2'][idx]['fat']             : 점심 메뉴 지방
        # res['data'][day]['2'][idx]['salt']            : 점심 메뉴 나트륨
        # res['data'][day]['2'][idx]['thumbnailUrl']    : 점심 메뉴 이미지 URL 
        for day in week:
            menus = data[day]["2"]
            date_data = date_data + datetime.timedelta(days=1)
            date = str(date_data).replace("-", "")
            for menu in menus:
                course = menu['corner']
                main_menu = menu['name']
                side_menu = menu['side']
                kcal = int(menu['kcal'])
                cho = int(menu['carb'])
                protein = int(menu['protein'])
                fat = int(menu['fat'])
                sodium = int(menu['salt'])
                image_url = menu['thumbnailUrl']
                # ==================================================================================================================
                # 데이터 분류
                # course    : 코스 (ex : 한식, 일식)
                # main_menu : 메인 메뉴
                # sub_menu  : 서브 메뉴
                # kcal      : 메뉴 칼로리
                # cho       : 메뉴 탄수화물
                # fat       : 메뉴 지방
                # protein   : 메뉴 단백질
                # image_url : 메뉴 이미지 URL

                # DB에 데이터 Insert
                cur.execute(f"SELECT * FROM lunch_menu where date='{date}' and main_menu='{main_menu}' and side_menu='{side_menu}' and region='{region}'")
                if (not cur.fetchall()):
                    cur.execute(f"INSERT INTO lunch_menu (date, region, course, main_menu, side_menu, kcal, cho, fat, protein, sodium, image_url) VALUES('{date}', '{region}', '{course}', '{main_menu}', '{side_menu}', '{kcal}', '{cho}', '{fat}', '{protein}', '{sodium}', '{image_url}')")
                else:
                    print("Duplicate Data")
                    return "Duplicate Data", 202
        # DB에 데이터 적용
        conn.commit()
        print("Done!")

        print("Success Insert Data")
        return "Success Insert Data" ,201
    else:
        print("Method Not Allowed")
        return "Method Not Allowed", 405

def lunch_data_crawling():
    print("점심메뉴 크롤링")
    url = "http://127.0.0.1:5000/lunch_menu"
    requests.get(url)

## python scheduler 실행
scheduler = BackgroundScheduler()
scheduler.start()

## Interval 매주 월요일 00:00마다 실행
scheduler.add_job(lunch_data_crawling, 'interval', weeks=1, start_date="2023-02-06 00:00:00", timezone="asia/seoul")

if __name__ == '__main__':
    app.run() 
