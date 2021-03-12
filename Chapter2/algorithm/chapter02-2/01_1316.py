# 백준 문제번호 - 1316

# N이 3이라고 가정한 후 풀이.
N = int(input())    # 단어 개수

group = 0 # 그룹단어 0으로 초깃값 설정

for i in range(N):  # N = 3 이라면 -> 0 ~ 2 
    num = input()   # N개 만큼 단어 입력 -> happy
    cnt = 0         # cnt -> 연속하지 않은 위치에 해당 단어가 존재하는 지 카운팅
    for j in range(len(num)-1): # -> happy의 length는 5
        if num[j] != num[j+1]:          # 0번째 인덱스와 1번째 인덱스가 다르면, (0번째 index는:h / 1번쨰 index:a)
                num_list = num[j+1:]    # 1번째 인덱스부터 모든 문자열을 num_list에 담는다. -> appy
                if num_list.count(num[j]) > 0:  # num_list에 0번째 인덱스와 같은 문자가 발견되면 (appy중 h가 위치한다면!?)
                    cnt += 1                    # 카운트에 +1을 해준다. -> cnt가 0보다 크다면 0번째 문자가 연속되지 않은 위치 어딘가에 위치함.
    if cnt == 0:    # cnt가 0이라면 -> 연속되지 않은 문자들 중 0번째 문자가 어디에도 위치하지 않음 -> 그룹단어 조건 성립
        group += 1

print(group)