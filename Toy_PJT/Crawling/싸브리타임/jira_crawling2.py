# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://ssafy.atlassian.net/rest/api/2/field"

auth = HTTPBasicAuth("junhong625@naver.com", "ATATT3xFfGF0k2hYB3fGvhUJH4o5IRwqEa9g8cDkNzahE-MrVHa4ht_ioDCLuSijoJs5yjpZNvPNbz9ywHjBPj6CzSuTEvsGhXTHWPsE9JpO2WCQFSTjdsaU227rRxZSITg-rq8PIbYgKEJLM2kxiYX_HoyECQkApXbrkEj3jiEUFCYRESUtPtE=79015900")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))