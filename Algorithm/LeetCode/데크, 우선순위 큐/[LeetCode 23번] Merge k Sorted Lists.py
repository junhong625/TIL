# heap을 이용한 풀이
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeKLists(self, lists):
        import heapq
        
        heap = []
        for l in lists:                                 # 연결리스트의 원소를 heap리스트 에 모두 저장
            while l:
                heap.append(l.val)
                l = l.next
        heapq.heapify(heap)                             # heap리스트를 heap자료구조로 변환
        
        head = tail = ListNode()                        # 빈 연결리스트 생성
        
        for i in range(len(heap)):                      # 정렬된 순서대로 작은 값부터 연결리스트 노드 생성 후 연결
            tail.next = ListNode(heapq.heappop(heap))
            tail = tail.next
        
        return head.next