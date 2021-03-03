s = "(())()"


def is_correct_parenthesis(string):
    check = []
    for letter in string:
        if letter == "(":
            check.append(0)
        elif letter == ")":
            if len(check) > 0:
                check.pop()
            else:
                return False
    if len(check) > 0:
        return False
    return True


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
