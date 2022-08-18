import sys

N = int(sys.stdin.readline())

total = 0                           # 산술평균을 구하기 위한 총합
sort_num = []                       # 중앙값과 범위를 구하기 위한 입력된 수들의 정렬
dict_num = {}                       # 최빈값을 구하기 위해 카운팅 정렬

for n in range(N):
    num = int(sys.stdin.readline()) # 숫자 입력
    total += num                    # 총합에 +
    sort_num.append(num)            # 정렬하기 위한 리스트에 추가
    if num in dict_num:             # 카운팅 정렬
        dict_num[num] += 1
    else:
        dict_num[num] = 1

sort_num = sorted(list(sort_num))   # 입력된 숫자 리스트 정렬


sort_dict = {}                      # 카운팅 정렬된 데이터를 key와 value를 서로 바꿔 재정렬
for key, value in dict_num.items():
    if value in sort_dict:
        sort_dict[value].append(key)
    else:
        sort_dict[value] = [key]

print(round(total / N))             # 산술평균 출력
print(sort_num[N//2])               # 중앙값 출력
print(sorted(sort_dict[max(sort_dict)])[1] if len(sort_dict[max(sort_dict)]) > 1 else sort_dict[max(sort_dict)][0]) # 최빈값 출력
print(sort_num[-1] - sort_num[0])   # 범위 출력 