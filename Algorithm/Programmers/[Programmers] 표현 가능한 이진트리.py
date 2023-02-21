flag = True                                 # 이진트리로 생성이 가능한지 불가능한지 판단하는 기준

## 이진트리로 변환가능한지 확인
def check_binary_tree(binary):
    if not binary:                          # 이진수가 존재하지 않을 경우 종료
        return
    global flag
    if flag == False:                       # 이진트리로 변환이 불가능할 경우 모든 재귀 종료
        return
    mid = len(binary)//2                    # 루트 노드 위치
    if binary[mid] == "1":                  # 루트 노드가 1일 경우
        check_binary_tree(binary[:mid])     # 루트 노드 기준 왼쪽 이진수
        check_binary_tree(binary[mid+1:])   # 루트 노드 기준 오른쪽 이진수
    else:                                   # 루트 노드가 0일 경우
        if sum(map(int, binary)):           # 루트 노드의 자식 노드들이 모두 0일 아닐 경우는 이진트리 생성 불가로 판단
            flag = False

def solution(numbers):
    answer = []
    global flag
    for num in numbers:
        binary = bin(num)[2:]               # 이진수로 변환 후 문자열 제거
        std = 2                             # 포화 이진 트리 개수 std-1
        while len(binary) > std-1:          # binary보다 큰 포화 이진 트리 개수 찾기 
            std *= 2                        
        binary = ("0"*(std-1-len(binary))) + binary # 부족한 더미 노드 삽입하여 포화 이진트리 생성
        flag = True                         # flag 초기화
        if binary[len(binary)//2] == "1":   # 루트 노드가 1일 경우에만 탐색 시작
            check_binary_tree(binary)       # 확인 작업 시작
        else:                               # 루트 노드가 0일 경우에는 불가능하다고 판단
            flag = False
        answer.append(1 if flag else 0)     # flag에 따라 answer 1 or 0 삽입
    return answer