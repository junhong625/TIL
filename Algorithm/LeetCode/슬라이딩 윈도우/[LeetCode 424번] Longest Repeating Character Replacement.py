class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt_cur = dict()                                                        # 문자들의 개수를 계산 할 dict
        cur = ""                                                                # 현재 문자열
        answer = 0                                                              # 최대 문자열 수
        
        for char in s:                                                          # s 순회
            cnt_cur[char] = cnt_cur.get(char,0) + 1                             # 문자 개수 + 1
            cur += char                                                         # cur에 문자 추가
            while True:                                                         # 문자 변동이 없을 경우 종료 되는 반복문
                if len(cnt_cur) > k+1 or len(cur) - max(cnt_cur.values()) > k:  # cnt_cur에 들어있는 문자의 종류가 k보다 많거나 cur에서 가장 많이 들어있는 문자의 개수를 뺀 값이 k보다 클 경우
                    cnt_cur[cur[0]] -= 1                                        # 제일 앞 문자 개수 -1
                    if not cnt_cur[cur[0]]:                                     # 제일 앞 문자의 개수가 0일 경우 cnt_cur에서 제거
                        del cnt_cur[cur[0]]                                     
                    cur = cur[1:]                                               # 제일 앞 문자 제거
                    continue                                                    # 다시 검사 실시
                break                                                           # 조건에 걸리지 않았다면 while문 종료
            answer = max(answer, len(cur))                                      # answer보다 cur이 짧을 경우 변경
        return answer                                                           # s 순회가 끝난 후 정답 반환
            