def solution(s):
    answer, dummy = [], []
    subset = ""
    for el in s[1:-1]:
        if el == "}":                           # 하나의 집합이 끝나는 부분
            dummy.append(subset.strip(","))     # ,를 제거 후 dummy에 subset 추가
            subset = ""                         # subset 초기화
        elif el != "{":                         # 끝나는 부분이 아니고 시작 부분을 제외한 모든 문자를 subset에 추가
            subset += el
    for i, v in enumerate(dummy):               # dummy를 순회
        dummy[i] = list(map(int, v.split(","))) # dummy에 들어있는 각각의 집합에서 문자들을 숫자로 변환
    dummy.sort(key=lambda x:len(x))             # 집합의 길이순에 따라 정렬
    for dum in dummy:                           # 각 집합의 원소를 하나씩 꺼내 중복으로 존재하지 않을 경우 answer에 추가
        for d in dum:
            if d not in answer:
                answer.append(d)
    return answer