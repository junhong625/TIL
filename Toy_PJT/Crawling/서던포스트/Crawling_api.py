import requests
import pandas as pd
import pprint
import time

data = pd.read_excel('TIL\Toy_PJT\Crawling\주소 크롤링.xlsx', dtype=object)
# data2 = pd.read_excel('market.xlsx')
print(data)



# phone = data['전화번호']
# name = data['점포명']
# address = data['주소']
# siID1 = data['siID1']

# phone_name = []
# phone_address = []

# for i in range(len(data)):
#     url = f'https://openapi.naver.com/v1/search/local.json?query={phone[i]}'
#     headers = {
#         'X-Naver-Client-Id' : 'uNJUXUTLhgkkz9vwC4Sd',
#         'X-Naver-Client-Secret' : 'CE8oetOZih'
#     }
    
    
#     res = requests.get(url, headers=headers).json()
# #     print(res)

#     if res:
#         if res['items']:
#             res = res['items'][0]
#             phone_name.append(res['title'])
#             phone_address.append(res['roadAddress'])
#             print(i+1, res['title'], res['roadAddress'])
#             continue
#     phone_name.append('검색 결과 없음')
#     phone_address.append('검색 결과 없음')
#     print(i+1, '검색 결과 없음')
#     time.sleep(0.5)
# #             print(name[i])
# #             if name[i] in res['title']:
# #                 for addr in data['주소'][i].split():
# # #                     print(addr)
# #                     if addr not in res['roadAddress']:
# #                         break
# #                 else:
# #                     match.append('O')
# #                     print('O')
# #                     siID1.append(data['siID1'])
# #                     continue
# #     match.append('X')

# ## 중간에 끊긴 이후 
# for i in range(9582, len(data)):
#     url = f'https://openapi.naver.com/v1/search/local.json?query={phone[i]}'
#     headers = {
#         'X-Naver-Client-Id' : 'uNJUXUTLhgkkz9vwC4Sd',
#         'X-Naver-Client-Secret' : 'CE8oetOZih'
#     }
    
    
#     res = requests.get(url, headers=headers).json()
# #     print(res)

#     if res:
#         if res['items']:
#             res = res['items'][0]
#             phone_name.append(res['title'])
#             phone_address.append(res['roadAddress'])
#             print(i+1, res['title'], res['roadAddress'])
#             continue
#     phone_name.append('검색 결과 없음')
#     phone_address.append('검색 결과 없음')
#     print(i+1, '검색 결과 없음')
#     time.sleep(0.5)
# #             print(name[i])
# #             if name[i] in res['title']:
# #                 for addr in data['주소'][i].split():
# # #                     print(addr)
# #                     if addr not in res['roadAddress']:
# #                         break
# #                 else:
# #                     match.append('O')
# #                     print('O')
# #                     siID1.append(data['siID1'])
# #                     continue
# #     match.append('X')
