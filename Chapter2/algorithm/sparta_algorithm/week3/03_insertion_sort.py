# 정렬 - 삽입정렬

input = [4, 6, 2, 9, 1]

def insertion_sort(array):
    n = len(array)

    # O(N^2)의 시간이 걸린다. 그러나 버블정렬과 선택정렬과는 다른 면이 있다. 바로 break문! -> 최선의 경우에는 N만큼의 시간 복잡도가 걸릴 수 있다.
    for i in range(1, n):   # 1 ~ 4
        for j in range(i):  # 0 / 0 ~ 1 / 0 ~ 2 / 0 ~ 3
            if array[i - j - 1] > array[i - j]:
                array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
            else:
                break

    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!