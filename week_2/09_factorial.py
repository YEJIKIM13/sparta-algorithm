def factorial(n):
    # 이 부분을 채워보세요!
    # 탈출조건, 특정 숫자로 떨어지는 조건이 있다. factorial(1) = 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))