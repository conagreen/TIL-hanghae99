# 백준 문제번호 - 2751

N = int(input())
num_list = []

for _ in range(N):
    num = int(input())
    num_list.append(num)

for i in sorted(num_list):
    print(i)