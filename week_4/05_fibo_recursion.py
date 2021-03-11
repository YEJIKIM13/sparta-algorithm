input = 20


def fibo_recursion(n):
    if n < 3:  # 아니면 if n == 1 or n == 2 라고 표현도 가능!
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765


# 재귀함수가 너무 깊어진다면...
"""
1. Fibo(3) 이라면
Fibo(2) 과 Fibo(1) 을 더하면 됨.
이는 1, 1 -> 연산량 2번

2. Fibo(4) 이라면
Fibo(3) 과 Fibo(2) 을 더하면 됨.
Fibo(3) ? 1번 과정을 반복하면 됨.
Fibo(2) -> 1 반환 
-> Fibo(3) + 1
   -> Fibo(2) + Fibo(1)
   -> 1 + 1
   -> 연산량 2번
-> 2 + 1
-> 연산량 2번 + 연산량 1번 = 연산량 3번

---반복---
"""