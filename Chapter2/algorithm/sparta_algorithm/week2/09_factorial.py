# 재귀함수 - 팩토리얼

# Factorial(N) = N * Factorial(N - 1)
# ....
# Factorial(1) = 1


# 5 * 4 * 3 * 2 * factorial(1) -> 5 * 4 * 3 * 2 * 1
def factorial(n):   # 1
    if n == 1:      # 1 == 1 -> o
        return 1

    return n * factorial(n - 1) # 2 * factorial(1)


print(factorial(5))