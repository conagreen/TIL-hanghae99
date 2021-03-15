# 백준 문제번호 - 11399

import sys

# N = 5 일 경우
N = int(input()) # N = 5
per_time = list(map(int, sys.stdin.readline().split())) # [3, 1, 4, 3, 2]

result = 0
per_time.sort()                 # 오름차순으로 정렬 [1, 2, 3, 3, 4]
for i in range(N):              # i -> 0 ~ 4
    for j in range(i+1):        # j -> 0 ~ i+1
        result += per_time[j]

print(result)
