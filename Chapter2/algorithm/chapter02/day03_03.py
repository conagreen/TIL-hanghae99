# 백준 문제번호 - 1929

def isPrime(num):
    if num == 1:    # 1은 소수도 합성수도 아님
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1): # 2 ~ num의 제곱근까지만 검사 ex) 9의 제곱근은 3
            if num % i == 0:
                return False
        return True

M, N = map(int, input().split())    # M:3 N:16

for i in range(M, N+1): # 3 ~ 16
    if isPrime(i):  # i:3
        print(i)
 
# 튜터님 코멘트 메모

# 1 * (x != 1)

# 이런 코드는 파이썬 문법을 이해해야만 이런 응답이 올 수 있다고 알 수 있는, 
# 언어 종속성이 강한 코드인 것 같습니다. 저는 이런 코드를 안 좋다고 생각하는 편이라, 
# 아 이런 것도 있구나~~  정도로 넘어가셔도 좋을 것 같습니다 ㅎㅎ

# print(1 * True)  # 1
# print(1 * False)  # 0