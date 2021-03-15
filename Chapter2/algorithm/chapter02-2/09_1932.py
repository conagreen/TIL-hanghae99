# 백준 문제번호 - 1932

# n이 5라고 가정
n = int(input())    # 삼각형의 크기 -> 5
t = []
for i in range(n):  # 0 ~ 4 변수 i에 반복문을 통해 저장
    t.append(list(map(int, input().split()))) # 정수삼각형 만들기
k = 2
for i in range(1, n):   # i -> t(리스트)의 인덱스 (1 ~ 4) 
    for j in range(k):  # j -> 값의 인덱스 (0 ~ 1 / 0 ~ 2 / 0 ~ 3 / 0 ~ 4)
                                    # i:    1     2        3       4    
        if j == 0:      # 맨 왼쪽 숫자
            t[i][j] = t[i][j] + t[i - 1][j]     # i:1 j:0
        elif i == j:    # 맨 오른쪽 숫자
            t[i][j] = t[i][j] + t[i - 1][j - 1] # i:1 j:1
        else:           # 중간 숫자
            t[i][j] = max(t[i - 1][j - 1], t[i - 1][j]) + t[i][j] # i:2 j:1
    k += 1
print(max(t[n - 1]))    # 마지막 인덱스의 숫자들 중 최댓값 출력