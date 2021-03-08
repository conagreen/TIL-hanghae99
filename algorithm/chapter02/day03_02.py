# 백준 문제번호 - 10250

# t = 테스트 데이터
# w = 각 층의 방 개수
# h = 층수
# n = 순서

t = int(input())

for i in range(t):
  h, w, n = map(int,input().split())

  # 호수 구하기
  line = n // h + 1

  # 사람수가 층수로 나누어질때
  if n % h == 0:    # 꼭대기 층
    floor = h
    line = n // h
  else:
    floor = n % h
  
  answer = floor * pow(10,2) + line # 10의 2승
  print(answer)