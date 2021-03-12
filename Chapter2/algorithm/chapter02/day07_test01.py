# 백준 문제번호 - 10815

cnt_card = int(input())
num_card = list(map(int, input().split()))

predicted_cnt = int(input())
predicted_num = list(map(int, input().split()))

num_card.sort()

for i in range(predicted_cnt):
    start, end = 0, cnt_card-1
    while start <= end:
        mid = (start + end) // 2
        if num_card[mid] == predicted_num[i]:
            print(1, end=" ")
            break
        elif num_card[mid] < predicted_num[i]:
            start = mid + 1                     
        else:
            end = mid - 1
        
        if start > end:
            print(0, end=" ")
            break