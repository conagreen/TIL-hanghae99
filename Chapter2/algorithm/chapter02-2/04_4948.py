# 백준 문제번호 - 4948

import math

def isPrime(num):      # 소수 분별하는 함수
    if num == 1: 
        return False   # 1은 소수도 합성수도 아님

    for i in range(2, int(math.sqrt(num))+1):   # Math.sqrt() 함수는 숫자의 제곱근을 반환 = int(num ** 0.5) + 1) <- 제곱근 구하는.....식인데 이해안됨
        if num % i == 0:                        # 1과 자기 자신을 제외한 다른 숫자로도 나누어떨어짐 ex) num이 9라면 1과 9외의 숫자로 나누어 떨어지는 게 존재하는가?
            return False         

    return True


li = list(range(2,246912))  # 미리 123456의 2배인 246912 사이에 있는 소수를 구해 그 리스트에서 비교
prime_li = []               # 빈 소수 리스트 생성
for i in li:
    if isPrime(i):
        prime_li.append(i)

while(1):
    answer = 0
    n = int(input())    # 1 ≤ n ≤ 123,456
    if n == 0: 
        break

    for i in prime_li:  # 246912 사이에 있는 모든 소수를 변수 i에 저장
        if n < i <= n*2: # n보다 크고, 2n보다 작거나 같은 소수의 개수 
            answer += 1

    print(answer)