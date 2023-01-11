import requests
import json

# url = "https://edu.ssafy.com/edu/mycampus/attendance/attendanceClassList.do"
# url = "https://edu.ssafy.com/edu/main/selectNtcnCnt.do?callback=myCallback&_=1673332005671"
url = "https://edu.ssafy.com/edu/main/selectNtcnCnt.do?callback=myCallback&_=1673335115136"
url = "https://edu.ssafy.com/edu/lectureroom/survey/surveyList.do"

headers = {
    'Content-Type':'application/json; charset=utf-8'
}
custom_header = {
    'referer' : 'https://edu.ssafy.com/edu/lectureroom/survey/surveyList.do',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'  }

cookies = {
    'JSESSIONID_HAKSAF':'21WaXA5I7x58_XfY-AR2OdDR9R96NxsuDF799XJi4KclUYRXQQI_!1495539031!-1564893934!1673332002376',
    'WMONID':'PDvqxEiRxpO'
}

data = {
    'searchStartDt' : '20230102', 
    'searchEndDt' : '20230201' 
}

# res = requests.post(url, headers=headers, cookies=cookies, data=data).json()
res = requests.get(url, headers=custom_header, cookies=cookies).text
print(res)