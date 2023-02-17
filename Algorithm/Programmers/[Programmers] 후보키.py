## 조합을 만들어내는 함수
# group : 조합
# arr   : 조합에 사용될 집합
# idx   : 시작 idx
# comb  : group이 들어갈 리스트
def combinations(group, arr, idx, comb):
    if group:
        comb.append(group[::])
    for i in range(idx, len(arr)):
        group.append(arr[i])
        combinations(group, arr, i+1, comb)
        group.pop()

## 후보키 확인 함수
# arr       : 후보키인지 확인할 column 번호 집합
# relation  : relation 데이터
def check_candidate(arr, relation):
    dup = [] # 중복되는 tuple이 있는지 확인하기 위한 리스트
    for i in range(len(relation)):
        sub = "" # tuple을 문자열 형식으로 변환하여 중복 체크
        for el in arr: 
            sub += relation[i][el]
        if sub in dup:  # 중복되는 tuple이 있을 경우
            return False
        dup.append(sub)
        sub = []
    return True # 모든 tuple에서 중복이 발견되지 않을 경우
    
## 문제 풀이 함수
def solution(relation):
    answer = 0
    comb = []
    combinations([], range(len(relation[0])), 0, comb)  # 조합 생성
    comb.sort(key=lambda x:len(x))  # 길이순으로 정렬
    candidate_key = []  # 후보키가 들어갈 리스트
    for case in comb:
        sub = []
        combinations([], case, 0, sub)  # 튜플의 조합 생성
        for el in sub:
            if el in candidate_key: # 튜플의 조합들 중 후보키에 포함되는 조합이 발견될 경우 최소성 조건 위배
                break
        else:
            if check_candidate(case, relation): # 후보키라고 판단할 경우
                candidate_key.append(case)  # 후보키에 추가
                answer += 1 # 후보키 개수 + 1
    return answer
    