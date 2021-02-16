input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 배열 초기화
    alphabet_occurrence_array = [0] * 26

    for char in string:
        # 알파벳인지 확인(특수기호 거르기 위해)
        if not char.isalpha():
            # 반복문의 다음 인덱스로 넘어가기 위해
            continue
        # 'a' -> 0, 'b' -> 1, 'c' -> 2 ...
        index = ord(char) - ord('a')
        alphabet_occurrence_array[index] += 1

    return alphabet_occurrence_array

result = find_max_occurred_alphabet(input)
print(result)