# 백준 문제번호 - 2869

# v = 나무 높이
# a = 달팽이가 낮에 올라갈 수 있는 높이
# b = 달팽이가 밤에 미끄러지는 높이

import sys
import math

a, b, v = map(int, sys.stdin.readline().split())
day = (v-b)/(a-b)

print(math.ceil(day))

# math를 사용하지 않는다면? 