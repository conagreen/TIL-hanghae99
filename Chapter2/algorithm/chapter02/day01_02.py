# 백준 문제번호 - 2588

# 방식1
a = int(input()) 
b = input()

R1 = int(b[2]) * a 
R2 = int(b[1]) * a
R3 = int(b[0]) * a
Result = int(b) * a

print(R1, R2, R3, Result, sep="\n")

# 방식2
a = int(input())
b = input()

b3 = b[::-1]

for n in b3:
    print(a * int(n))

print(a * int(b))