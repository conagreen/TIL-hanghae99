# 백준 문제번호 - 9184

# 방식1(고통의 3차원 배열....) 도움 - 치호

# # cache[0][0][0] ~ cache[20][20][20]
# # 0으로 초기화
# cache = [[[0 for col in range(21)] for row in range(21)] for depth in range(21)]

# # 1. 일단 문제 그대로 따라서 만듬
# # 2. 실행 & 분석 -> 중복
# # 3. 중복을 어떻게 제거 할 것인가?

# def w(a, b, c):
#     if cache[a][b][c] == 0:
#         if a <= 0 or b <= 0 or c <= 0:
#             return 1
#         if a > 20 or b > 20 or c > 20:
#             return w(20, 20, 20)
#         if a < b < c:
#             cache[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
#             return cache[a][b][c]
#         else:
#             cache[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
#             return cache[a][b][c]
#     return cache[a][b][c]


# if __name__ == '__main__':
#     result = w(15, 15, 15)
#     print(result)

# 방식 2 (딕셔너리)