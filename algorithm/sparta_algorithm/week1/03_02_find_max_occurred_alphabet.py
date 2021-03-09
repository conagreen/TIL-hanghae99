# 최빈값 찾기 방식2

input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")    # 아스키 코드를 이용하여 계산한 후 -> 각 알파벳을 순서대로 alphabet_occurrence_array 변수에 담는다.
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0          # 가장 많이 발생했던 빈도수를 저장하는 변수
    max_alphabet_index = 0      # 가장 많이 나왔던 알파벳의 인덱스를 저장하는 변수
    for index in range(len(alphabet_occurrence_array)):
        # index 0 -> alphabet_occurrence 3
        alphabet_occurrence = alphabet_occurrence_array[index]
        
        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence
    
    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)