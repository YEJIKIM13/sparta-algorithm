# 반복되는 구조로 문제가 점점 작아지는 것을 인식하고 그걸 함수로 만들면 재귀 함수로 해결할 수 있다!!!
# 문제가 점점 반복 -> 반복되는 속에서 해결되는 구조가 있으면, 아 재귀함수로 풀면 되겠구나 라고 생각!
# 재귀 함수로 풀 때는 항상 탈출조건 적어주는 것 잊지 말기!

input = "여보게저기저게보여"


def is_palindrome(string):
    # 탈출조건
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    # 안에서 부르고 또 부르고 부르고 또 부르고...
    # 앞 뒤 하나씩 없애나가기!
    return is_palindrome(string[1:-1])


print(is_palindrome(input))