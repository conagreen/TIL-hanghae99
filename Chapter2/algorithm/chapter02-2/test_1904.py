# 백준 문제번호 - 1904

n = int(input())                # 1 <= n <= 1,000,000

n_list = [0] * 1000001          # 0 ~ 1000000
n_list[1], n_list[2] = 1, 2     # 인덱스 0은 사용하지 x

for i in range(3, n+1):
    n_list[i] = (n_list[i-2] + n_list[i-1]) % 15746

print(n_list[n])

'''
n = 1 -> 1
n = 2 -> 11 00
n = 3 -> 111 100 001
n = 4 -> 1111 1100 1001 0011 0000
.
.
.

n = 1 이면 1개, n = 2 이면 2개, n = 3 이면 3개, n = 4 이면 5개, n = 5 이면 8개 ...

피보나치 수열의 규칙이 존재한다.

피보나치 수열을 수학 공식으로 나타내면 다음과 같다.

f(n) = 1 (n＜=2 일 때)
f(n) = f(n-2)+f(n-1) (n＞2 일 때)

즉, 피보나치 수열을 생성하는 기본 규칙은 처음 두 항은 1이고, 세 번째 항부터는 바로 앞의 두 항의 합이 된다는 것이다.
이 규칙을 이해한다면 큰 어려움 없이 해결할 수 있다.
'''