input = 20

# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다
# 주어진 자연수 n이 소수이기 위한 필요 충분 조건은 n이 n의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다
# 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중 하나는 반드시 n의 제곱근 이하라는 의미
# 반드시 n의 제곱근 이
def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        # 2 ~ n-1 에서 소수인 친구들만 검사해도 됨
        for j in prime_list:  # range(2, n) 대신에
            if n % j == 0 and j * j <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
