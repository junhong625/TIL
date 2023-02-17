# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://ssafy.atlassian.net/'
name = '안준홍'
token = 'ATATT3xFfGF0Fuf0PgAtxeEM0guWXiZ3IY-OVX2HXoPN6TTQM43j9AEZCPNduZ0ym4R8zIvfd016Nv9kj2THff6Xq54K1pUEaGBHHINjqytvaWyul9nezwRY65nO5Uvk9uikBeeqlNGx3WSJR64tQfQc8TWLCLJC96IHgaLzMnzhKQbuQDZMNu4=4754A56E'
proj = 'S08P12A602'
jql = f"project={proj} and assignee={name} and status not in (closed, done)"

url = f"https://ssafy.atlassian.net/rest/api/3/search"

auth = HTTPBasicAuth("junhong625@naver.com", "ATATT3xFfGF0Fuf0PgAtxeEM0guWXiZ3IY-OVX2HXoPN6TTQM43j9AEZCPNduZ0ym4R8zIvfd016Nv9kj2THff6Xq54K1pUEaGBHHINjqytvaWyul9nezwRY65nO5Uvk9uikBeeqlNGx3WSJR64tQfQc8TWLCLJC96IHgaLzMnzhKQbuQDZMNu4=4754A56E")

headers = {
  "Accept": "application/json"
}

query = {
  'jql' : jql
}

issues = requests.get(url=url, headers=headers, params=query, auth=auth).json()['issues']
issue_list = []
for issue in issues:
    # print(issue)
    issue_list.append(issue['fields']['summary'])

print({'issue_list':issue_list})
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))