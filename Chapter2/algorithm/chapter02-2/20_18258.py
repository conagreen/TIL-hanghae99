# 백준 문제번호 - 18258

import sys
from collections import deque

def push(queue, x):     # 정수 x를 큐에 넣는 연산이다.
    queue.append(x)
    
def pop(deque):         # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    return deque.popleft() if deque else -1 

def size(queue):        # 큐에 들어있는 정수의 개수를 출력한다.
    return len(queue)

def empty(queue):       # 큐가 비어있으면 1, 아니면 0을 출력한다.
    return 1 if not queue else 0

def front(queue):       # 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    return queue[0] if queue else -1

def back(queue):        # 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    return queue[-1] if queue else -1

deque = deque()

N = int(sys.stdin.readline().rstrip())  # 명령의 수

for _ in range(N):
    order = sys.stdin.readline().split()
    
    command = order[0]
    
    if(command == "push"):
        push(deque, order[1])
    elif(command == "pop"):
        print(pop(deque))
    elif(command == "size"):
        print(size(deque))
    elif(command == "empty"):
        print(empty(deque))
    elif(command == "front"):
        print(front(deque))
    elif(command == "back"):
        print(back(deque))