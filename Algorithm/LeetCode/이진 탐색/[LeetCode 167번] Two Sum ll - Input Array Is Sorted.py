class Solution:
    def twoSum(self, numbers, target) -> list:
        
        result = None
        
        ## 이진 탐색 함수
        def binarysearch(idx):
            target_2 = target - numbers[idx]        # 이진 탐색에서 찾아야 할 목표
            
            start, end = idx+1, len(numbers)-1      # 순차 탐색을 할 것이기에 idx의 다음 범위만 이진 탐색
            
            while start <= end:                     # 시작점과 끝점이 서로 지나치기 전까지 반복
                mid = (start+end)//2                # 중간 idx
                if target_2 < numbers[mid]:         # 중간 idx의 값이 목표보다 클 경우
                    end = mid - 1                   # 끝 포인터 이동
                elif target_2 > numbers[mid]:       # 중간 idx의 값이 목표보다 작을 경우
                    start = mid + 1                 # 시작 포인터 이동
                else:                               # 목표와 중간 값이 같을 경우
                    nonlocal result                 # result 호출
                    result = sorted([idx+1, mid+1]) # result에 정답 할당
                    return
            
        for i in range(len(numbers)):               # 시작점부터 끝까지 순회
            binarysearch(i)                         # 이진 탐색
            if result:                              # result에 값이 들어가면
                return result                       # result를 반환하고 종료
        