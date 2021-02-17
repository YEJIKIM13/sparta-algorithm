input = 20

# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다
def find_prime_list_under_number(number):
    prime_list = []
    for i in range(2, number + 1):
        # 2 ~ n-1 에서 소수인 친구들만 검사해도 됨
        for j in prime_list:  #range(2, i)
            if i % j == 0:
                break
        else:
            prime_list.append(i)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
