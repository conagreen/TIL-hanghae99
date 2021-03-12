# 백준 문제번호 - 2164

from collections import deque

N = int(input())
deq = deque()

for i in range(N):
    deq.append(i+1)

while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())

print(deq.pop())