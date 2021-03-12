# 백준 문제번호 - 1011

# 방식 1 (참고 - https://ooyoung.tistory.com/91)
t = int(input())

for _ in range(t):
    x, y = map(int,input().split()) # x: 현재위치 / y: 목표위치
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리 / 빈도수
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    print(count)


# 방식 2 (참고 - https://data-jj.tistory.com/36)
import math

N = int(input())

count = 0                                    #최소 작동 횟수
result = []

for _ in range(N):
    a, b = map(int, input().split())
    distance = b - a                         #주어진 값들간의 거리

    num = math.floor(math.sqrt(distance))  #주어진 값들 사이의 거리에 루트 씌움 (제곱근) , floor처리되어 이미 정수임    
    num_jegob = num**2                # 정수를 제곱근으로 갖는 제곱수(ex. 9 : 9의 제곱근은 3)

    if distance == num_jegob:
        count = (num*2)-1

    elif num_jegob < distance <= num_jegob + num:
        count = (num*2)

    elif (num_jegob + num) < distance:
        count = (num*2) + 1

    elif distance < 4:
        count = distance
    result.append(count)



for x in result:
    print(x)