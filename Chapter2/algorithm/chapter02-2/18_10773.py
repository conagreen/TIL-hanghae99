# 백준 문제번호 - 10773

from sys import stdin


K = int(input())
stack = []

for _ in range(K):
    num = int(input())

    if(num == 0):           # 입력값이 "0" 일 경우에는 가장 최근에 쓴 수를 지우고,
        stack.pop()
    else:
        stack.append(num)   # 아닐 경우 해당 수를 쓴다.

print(sum(stack))