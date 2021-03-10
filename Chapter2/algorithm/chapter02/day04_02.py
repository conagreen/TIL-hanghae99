# 백준 문제번호 - 11651

num = int(input())  # 점의 개수 입력받기
temp_list = []

for i in range(num):
    [x, y] = map(int, input().split())
    reversed = [y, x]
    temp_list.append(reversed)   

sorted_list = sorted(temp_list)   # sorted라는 정렬함수는 시퀀스 자료형 뿐만 아니라 순서에 구애받지 않는 자료형에도 적용할 수 있고, 정렬된 결과는 list로 반환한다.
for i in range(num):
    print(sorted_list[i][1], sorted_list[i][0]) # [y, x] 형태로 저장 -> [1]은 x, [2]는 y 즉, x y 형태로 출력.