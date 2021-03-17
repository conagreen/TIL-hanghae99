# 백준 문제번호 - 1010

# 방식1 - 조합공식(combination)

'''
m이 n보다 크기 때문에 최대 연결할 수 있는 다리의 개수는 n개이고
m개의 지역에 n개의 다리를 놓을 수 있는 경우의 수를 구하는 것이기 때문에
mCn 으로 표현할 수 있고 이는 m! 을 (m-n)!n! 으로 나눈 값이 된다.
'''

def factorial(n):   # factorial을 표현하기 위한 함수
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridge)


# 방식2 - math.factorial 활용

import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)