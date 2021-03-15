# 백준 문제번호 - 1934

n = int(input())    # 테스트 케이스 개수 입력
for _ in range(n):  # 테스트 케이스 만큼 반복
    a, b = map(int, input().split())

    #기존의 값을 복사해둠
    x = a
    y = b
    
    while b != 0:
        r = a % b
        a = b
        b = r
    gcd = a
    lcd = x * y / a
    print(int(lcd))