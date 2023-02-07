from itertools import combinations
import requests, json, base64

url = "https://meeting.ssafy.com/s08public/channels/job8notice/api/v4/users/login"

login_id = "junhong625@naver.com"
password = "@Kaka21516!"

data = {'login_id' : login_id, 'password' : password}

result = requests.post(url=url, json=data).json()
# password = str.encode('UTF-8')
# password = base64.b64decode(password)
# print(password.decode('ascii'))
