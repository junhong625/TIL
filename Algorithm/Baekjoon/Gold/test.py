import requests
import json

date = '20230109'
url = f"https://welplus.welstory.com/api/meal?menuDt={date}&menuMealType=2&restaurantCode=REST000133"
headers = {
    'WCPCID':'05d9e831-ece6-6287-4942-c6a057d97ae3-1673253139935',
    'cafeteriaActiveId':'REST00013',
    'cafeteriaActiveName':'%EB%A9%80%ED%8B%B0%EC%BA%A0%ED%8D%BC%EC%8A%A4', 'JSESSIONID':'xbeVu7nEnn5WgvksySqd6ieFM3PEKX9VQk0cWNk12yfwN_pGjuZT!1386531071!822393198'

}

res = requests.get(url, headers=headers)

print(res)