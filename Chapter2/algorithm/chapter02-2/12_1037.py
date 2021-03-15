# 백준 문제번호 - 1037

# N = 2
N = int(input())                                # N: 16

div_list = list(map(int, input().split()))      # 16의 약수 -> 1 2 4 8 16 / 1과 N을 제외한 약수 입력 ->  2 4 8
div_max = max(div_list)
div_min = min(div_list)

print(div_max * div_min)