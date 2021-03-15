# 백준 문제번호 - 2609

a = list(map(int,input().split()))      # a = [24, 18]
a.sort()                                # a = [18, 24]
b = a.copy()                            # b = [18, 24]

while True: 
    if a[1] % a[0] == 0: 
        print(a[0])                     # 최대공약수 (6)
        ans = a[0]                      # ans = 6
        for n in b:                     # n -> 18, 24
            ans = ans * int(n / a[0])   # 6 * (18/6) ///////// 18 * (24/6)
        print(ans)                      # 최소공배수 
        break 
    else: 
        a[1] = a[1] % a[0]              # a = [18, 6]
    a.sort()