# 최댓값 찾기 
# 방식2 - 지정 변수

input = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    
    return max_num


result = find_max_num(input)
print(result)