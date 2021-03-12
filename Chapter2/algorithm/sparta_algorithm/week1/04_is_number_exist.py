# 점근 표기법 : 알고리즘의 성능을 수학적으로 표기하는 방법. 알고리즘의 "효율성"을 평가하는 방법.

# 점근 표기법의 종류
# 1. 빅오(Big-O) 표기법 - 최악의 성능이 나올 때 어느 정도의 연산량이 걸릴 것인지,
# 2. 빅 오메가(Big-Ω) 표기법 - 최선의 성능이 나올 때 어느 정도의 연산량이 걸릴 것인지에 대해 표기.

# 배열에서 특정 요소 찾기
input = [3, 5, 6, 1, 2, 4]

def is_number_exist(number, array):
    for element in array:       # array의 길이만큼 아래 연산이 실행
        if number == element:   # 비교 연산 1번 실행
            return True         # 총 시간복잡도 -> N X 1 -> 즉, N 만큼의 시간 복잡도가 걸렸다.
    
    return False

result = is_number_exist(3, input)
print(result)