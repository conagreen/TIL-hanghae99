# 알파벳 빈도수 세기 (아스키 코드 이용) 

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")    # 아스키 코드를 이용하여 계산한 후 -> 각 알파벳을 순서대로 alphabet_occurrence_array 변수에 담는다.
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array

print(find_alphabet_occurrence_array("hello my name is sparta"))
