# 재귀함수 - 자기 자신을 호출함으로써 코드를 간결하고 명확하게 만들 수 있다!

def count_down(number):
    if number < 0:         # 재귀 함수를 하기 위해서는 탈출 조건이 있어야 한다.
        return
    print(number)          # number를 출력하고

    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60) 