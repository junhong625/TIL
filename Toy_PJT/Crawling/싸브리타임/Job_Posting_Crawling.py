from itertools import combinations
import requests, json, base64

url = "https://meeting.ssafy.com/s08public/channels/job8notice/api/v4/users/login"

login_id = "junhong625@naver.com"
password = "@kaka21516!"
string = login_id+":"+password

data = {'login_id' : login_id, 'password' : password}

# result = requests.post(url=url, json=data).json()
password = string.encode('utf-8')
password = base64.b64encode(password)
print(password.decode('utf-8'))
