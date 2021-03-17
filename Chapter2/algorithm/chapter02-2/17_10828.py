# 백준 문제번호 - 10828

import sys              # sys.stdin.readline() 이 아닌 input() 함수 이용 시, 시간 초과 에러가 뜬다.

def push(x):            # 정수 x를 스택에 넣는 연산이다.
    stack.append(x)

def pop():              # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if not stack:
        return -1
    else:
        return stack.pop()

def size():             # 스택에 들어있는 정수의 개수를 출력한다.
    return len(stack)

def empty():            # 스택이 비어있으면 1, 아니면 0을 출력한다.
    return 0 if stack else 1

def top():              # 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    return stack[-1] if stack else -1

N = int(sys.stdin.readline())
stack = []              # 빈 리스트 생성. (파이썬의 리스트가 기본적으로 stack 구조를 따른다.)

for _ in range(N):
    input_split = sys.stdin.readline().split()

    order = input_split[0]

    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())