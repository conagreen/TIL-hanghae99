# 백준 문제번호 - 2108

# 방식1
import sys
n = int(input())
l = []

for _ in range(n):
    l.append(int(sys.stdin.readline()))

l.sort()

print('%d'%(round(sum(l)/n, 0)))                            # 산술평균
print(l[n//2])                                              # 중앙값

x = {}                                                      # 딕셔너리 생성

for i in l:                                                 # 빈도수 저장
    if i in x:
        x[i] += 1
    else:
        x[i] = 1
x = sorted(x.items(), key=lambda x : x[1], reverse = True)  # 빈도수를 기준으로 오름차순 정렬

if n != 1: 
    if x[0][1] == x[1][1]:                                  # 최빈값이 여러 개 있다면 최빈값 중 두번째로 작은값 출력
        print(x[1][0])
    else: print(x[0][0])
else:
    print(x[0][0])

print(max(l) - min(l))                                      # 범위


# 방식2 - Counter()함수 사용

import sys
from collections import Counter

N = int(sys.stdin.readline())
li = []
for _ in range(N):
    li.append(int(sys.stdin.readline()))


# 산술평균 (소숫점 첫째자리에서 반올림)
print(round(sum(li)/len(li)))

# 중앙값
li.sort()
print(li[(N-1)//2])

# 최빈값
if N == 1:
    print(li[0])
else:
    c = Counter(li).most_common(2)
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])

# 범위
print(li[-1] - li[0])
