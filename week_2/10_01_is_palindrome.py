input = "abcba"


def is_palindrome(string):
    # 조건 잘 설정!!! i가 뭐부터인지 체크해야지.
    for i in range(len(string) // 2):
        if string[i] != string[-(i+1)]:
            return False
    return True

    # n = len(string)
    # for i in range(n):
    #     if string[i] != string[n - 1 - i]:
    #         return False
    # return True


print(is_palindrome(input))