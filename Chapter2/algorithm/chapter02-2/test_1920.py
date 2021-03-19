# 백준 문제번호 - 1920

import sys

def find_num(n, m):
    for i in range(m):
        start, end = 0, n-1
        while start <= end:
            mid = (start + end) // 2
            if num1[mid] == num2[i]:
                print(1)
                break
            elif num1[mid] < num2[i]:
                start = mid + 1
            else:
                end = mid - 1
            
            if start > end:
                print(0)
                break

n = int(input())
num1 = list(map(int, sys.stdin.readline().split()))
m = int(input())
num2 = list(map(int, sys.stdin.readline().split()))

num1.sort()

find_num(n, m)