# 백준 문제번호 - 11047

# 해당 코드는 python3으로 채점을하면 시간초과가 나오지만 pypy3으로 제출하면 통과가 된다... 정신승리로 넘어가자...
import sys

N, K = map(int, sys.stdin.readline().split()) # N:동전 개수 / K:액수 합
types = []

for i in range(N):
    types.append(list(map(int, sys.stdin.readline().split())))
        
count = 0
for i in range(N):
    if K >= types[N-i-1][0]:
        while K >= types[N-i-1][0]:
            K -= types[N-i-1][0]
            count+=1

print(count)



# 그리디 알고리즘

#동전과 값 입력받기
n,k=map(int,input().split())
#동전을 입력받을 리스트 초기화하기
coin=[]

#동전 종류 입력받기
for i in range(n):
  coin.append(int(input()))

#동전개수 셀 변수 초기화
result=0

#동전 내림차순으로 정렬하기
coin.sort(reverse=True)

#동전 개수 구하기
for i in coin:
  if k==0: break
  result += k // i
  k %= i
  

print(result)
