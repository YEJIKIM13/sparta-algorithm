input = 20


def fibo_recursion(n):
    if n < 3:  # 아니면 if n == 1 or n == 2 라고 표현도 가능!
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765
