# 문제: 모든 조직원의 수익 파악하기

# 조건: 1) 1 <= len(enroll) <= 10000
#      2) len(referral) == len(enroll)
#      3) 1 <= len(seller) <= 100000
#      4) len(amount) == len(seller)
#      5) 칫솔 가격 = 100

# 방법: 1) union 재귀를 통해서 10%를 뺀 수익금만 해당 조직원 금액에 추가하기

def union(recommend, seller_no, answer, s, m): # 방법 1
    if m == 0:
        return
    pay = m // 10
    profit = m - pay
    answer[seller_no[s]] += profit
    if recommend.get(s):
        union(recommend, seller_no, answer, recommend.get(s), pay)
        

def solution(enroll, referral, seller, amount):
    recommend = {}
    seller_no = {}
    
    for i in range(len(referral)):
        if referral[i] != "-":
            recommend[enroll[i]] = referral[i]
        seller_no[enroll[i]] = i
    
    answer = [0] * len(enroll)
        
    for i in range(len(seller)):
        union(recommend, seller_no, answer, seller[i], amount[i] * 100)
    
    return answer