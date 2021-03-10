# 순차 탐색

finding_target = 19
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_sequential(target, array):
    find_count = 0
    for number in array:
        find_count += 1
        if target == number:
            print(find_count)
            return True
    print(find_count)
    return False

# 최악의 경우는 맨 끝까지 찾아야 되기 때문에 빅오 표기법으로 O(N)만큼의 시간 복잡도가 걸림.

result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True 