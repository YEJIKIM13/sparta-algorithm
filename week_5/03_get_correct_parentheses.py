from collections import deque

balanced_parentheses_string = "()))((()"


# deque 를 이용해서 구현
# 균형잡힌 괄호 문자열 -> 올바른 괄호 문자열
# 올바른 괄호 문자열? 어떻게 알았지?
def is_correct_parenthesis(string):  # 올바른 괄호 문자열인지 확인해주는 함수
    stack = []
    for s in string:  # 문자열에 문자를 하나하나 열린건지 비교
        if s == '(':  # 열려있는 거면 스택에 추가
            stack.append(s)
        elif stack:
            stack.pop()
    # 문자열이 끝났는데 스택에 아무것도 안 남아 있다면 올바른 문자열인지 확인 가능
    return len(stack) == 0


# 4번도 함수로 또 따로 빼줬음
def reverse_parenthesis(string):
    reversed_string = ""  # 이라는 변수에다가 그 문자를 담기 (단순히 뒤집는 게 아니라 괄호를 뒤집는거라서 일일이 해줘야함..)
    for char in string:  # u를 돌아가면서 뒤집어 주는 방븝 == u를 하나씩 문자를 반환하면서 바꿔줌 (단, 조건 4-4에 맞게)
        if char == "(":
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string


# 함수로 따로 빼줬음
# 큐로 똑같이 스트링을 만들어서 반환을 u, v로 해주는 방식
def separate_to_u_v(string):
    # 큐라는 변수에 문자열을 덱에 담아서 저장
    queue = deque(string)
    left, right = 0, 0  # 왼쪽과 오른쪽 괄호 0, 0으로 초기화
    u, v = "", ""  # u 랑 v 를 쪼개야 하니까 빈 문자열로 초기화
    # 큐에서 하나하나 빼면서 여는 소괄호와 닫는 소괄호의 개수가 똑같아야 함
    while queue:  # 큐가 끝나지 않을 때까지
        char = queue.popleft()
        u += char  # u 에다가 해당하는 char 를 하나씩 증가시켜주면 되겠지!
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break  # 함수를 멈춘다 ->
            # 멈추는 이유, u 같은 경우는 균형잡힌 괄호 문자열이 더 이상 분리할 수 없어야 된다고 했음.
            # u가 균형잡힌 문자열이 안 되게 하려면 여기서 더 이상 쌍이 안 생기도록 맨 처음에 left 와 right 가 맞았을 때 멈추도록 만들어줘야함
    v = ''.join(list(queue))
    return u, v


# 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
def change_to_correct_parentheses(string):
    if string == "":
        return ""
    # 2. 문자열 w 를 두 "균형잡힌 괄호 문자열" u,v 로 분리한다.
    # 단, u는 "균형잡힌 괄홓 문자열"로 더 이상 분리할 수 없어야 하며
    # v 는 빈 문자열이 될 수 있다. -> 그러면 어떻게 하면 문자열 w를 "두 균형잡힌 괄호 문자열"로 분리할 수 있을까?
    # 균형잡힌 괄호 문자열 -> 여는 소괄호 ( 와 닫는 소괄호 ) 의 개수가 같아야 한다는 것 <- 이 조건 먼저 만족하는 문자열을 꺼내보자
    u, v = separate_to_u_v(string)  # 받아서 가져오자

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해
    # 1단계부터 다시 수행합니다.
    # 즉 change_to_correct_parenthesis 를 다시 수행한다는 의미! (1번부터 조건이 시작되는데, 그 함수를 재귀적으로 다시 호출해주면 된다는 의미)
    # 근데 "올바른 괄호 문자열" 이란 조건이 있었음 -> 올바른 괄호 문자열을 확인하는 함수는 이미 만들어 놓음.
    # 3-1 조건: 수행한 결과 문자열을 u에 이어붙인 뒤 반환한다
    if is_correct_parenthesis(u):  # 문자열 u를 넣고 만약에 문자열이라면 v에 대해서 1단계부터 다시 수행합니다.
        return u + change_to_correct_parentheses(v)  # 즉 u랑 방금 말한 이 문자열 v에 대해서 1단계부터 수행한 결과를 붙여서 봔한

    # 4. 문자열 u가 올바른 괄호 문자열이 아니라면 (조건!! -> else) 아래 과정을 수행
    # 4-1. 빈 문자열에 첫 번째 문자로 ( 을 붙임
    # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다
    # 4-3. ) 를 다시 붙인다.
    # 4-4. u의 첫 번째 문자와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
    else:
        return "(" + change_to_correct_parentheses(v) + ")" + reverse_parenthesis(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):  # 들어온 문자열이 애초부터 올바른 문자열이라면
        return balanced_parentheses_string  # 그냥 그대로 반환
    else:  # 올바른 괄호 문자열 아닐 때, 균형잡힌 괄호 문자열일 때 바꾸는 방법 문제에 쓰여있는 대로 구현!!
        return change_to_correct_parentheses(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
