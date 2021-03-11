input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

# 피보나치 수열이 너무 부분 문제를 많이 발생하는 구조다 보니 이를 해결하기 위한 효율적인 방법인 다이나믹 프로그래밍!
# 원칙 두 가지 1)부분문제(반복되는 형태로 문제가 계속해서 파생된 게 있다면) 2)다이나믹 프로그래밍 하려면 메모이제이션 해야겠다! 메모 만들어야겠다!
# fibo_memo 를 이용하면서 올바르게 피보나치 수열을 반환해 줄 수 있을 것인가?!
# 1. 만약 메모에 있으면 그 값을 바로 반환하고
# 2. 없으면 아까 수식대로 구한다.
# 3. 그리고 그 값을 다시 메모에 기록한다.
# n 은 100부터 시작 Fibo(100) -> Fibo(99) -> Fibo(98) -> ... 위에서 아래로 내려가는 Top Down 방식
# Fibo(1) -> Fibo(2) -> Fibo(3) -> ... Bottom Up 방식


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo  # fibo_memo 에 기록하기
    return nth_fibo  # 기록 후 반환하기


print(fibo_dynamic_programming(input, memo))
