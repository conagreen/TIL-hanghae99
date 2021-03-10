# 최댓값 찾기
# 방식1 - 다른 숫자들과 비교하는 방식

input = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    for num in array:
        for compare_num in array:   # for else문: else문은 for문이 다 끝날 때까지 break 부분이 한 번도 나오지 않았다면 실행. 
            if num < compare_num:
                break
        else:
            return num

result = find_max_num(input)
print(result)