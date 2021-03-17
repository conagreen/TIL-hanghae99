# 백준 문제번호 - 9012

testCase = int(input()) 

for _ in range(testCase): 
    stack = [] 
    vps = input() 
    check = 0 
    for c in vps: 
        if c =='(': 
            stack.append(c)         # '('가 입력되었을 땐 append, ')'가 입력되었을 땐 pop -> stack의 length가 0이라는 건 VPS라는 의미
        elif c ==')': 
            if len(stack) == 0: 
                print('NO')         # 리스트 stack에 ')'가 먼저 입력되었다는 의미 
                check = 1           # check = 1 -> 결과 프린트 완료
                break 
            else: stack.pop(-1)

    if len(stack) != 0 and check == 0: 
        print('NO') 
    elif len(stack) == 0 and check == 0: 
        print('YES')