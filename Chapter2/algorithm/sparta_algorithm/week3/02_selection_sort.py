# 정렬 - 선택정렬

input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)          # 시간복잡도: 2차 반복이 나왔고 n의 길이만큼 반복한다. -> O(N^2)
    for i in range(n-1):    # 0 ~ 3 
        min_index = i
        for j in range(n-i):
            if array[i+j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!