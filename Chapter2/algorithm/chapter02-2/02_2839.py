# 백준 문제번호 - 2839

sugar = int(input())    # 상근이가 배달해야 할 설탕 무게

bag = 0 # 봉지 개수 0으로 초깃값 설정

while sugar >= 0 :
    if sugar % 5 == 0 :     # 5의 배수일 경우
        bag += (sugar // 5) # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  # 5로 나누어서 딱 떨어질 때까지 3kg을 빼준다. -> 5의 배수가 될 때까지
    bag += 1    # 설탕 -3kg -> 3kg봉지 +1
else :
    print(-1)   # 7처럼 5와 3으로 나누어지지 않다면 -1 출력