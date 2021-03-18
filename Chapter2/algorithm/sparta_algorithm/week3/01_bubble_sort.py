# 정렬 - 버블정렬

input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)  # 시간복잡도: 2차 반복이 나왔고 n의 길이만큼 반복한다. -> O(N^2)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(j)
    return

bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!