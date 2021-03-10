# 이진 탐색 (업다운 게임을 그대로 구현하면서 적용) 

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 1단계 - 최솟값:1              추측 값:8                       최댓값:16   -> 찾고자 하는 건 14 이므로 추측 값 보다 큼 
# 2단계 -                         최솟값:9    추측 값:12        최댓값:16   -> 여전히 타겟보다 작음
# 3단계 -                                       최소:13 추측:14 최대:16   -> 타겟 찾음

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2
    find_count = 0

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2

    print(find_count)
    return False

# 이진 탐색 vs 순차 탐색 -> 시간 복잡도 비교

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)