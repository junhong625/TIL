def solution(id_list, report, k):
    r1 = [i.split()[1] for i in set(report)]                        # 신고당한 사람만 r1에 저장
    r2 = [i for i in set(r1) if r1.count(i) >= k]                   # r1에 k개 이상 존재하는 사람만 r2에 저장(유저 게시판 이용 정지)
    r3 = [i.split()[0] for i in set(report) if i.split()[1] in r2]  # report에서 r2에 존재하는 사람을 신고한 사람들만 r3에 저장
    return [r3.count(i) for i in id_list]                           # id_list순서대로 순회하며 r3에 저장되어 있는 개수만큼 반환한 값을 저장한 리스트를 반환