input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 전, 후가 0이 아니라면 곱셈이 유리, 0이 포함되어 있다면 덧셈 유리할 것이다!
    # 1도 곱하는 것보다 더하는 게 더 크다!
    # 숫자를 돌면서 나온 각각의 숫자가 1보다 작거나 같다면 그냥 더하는 게 낫고, 1보다 크다면 곱하는 게 더 낫다
    multiply_sum = 0  # 현재 계산하고 있는 합계 정의
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number

    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)