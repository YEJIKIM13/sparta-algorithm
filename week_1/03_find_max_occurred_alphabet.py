input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        index = ord(char) - ord('a')
        alphabet_occurrence_array[index] += 1

    nth = 0
    for index in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[index] > alphabet_occurrence_array[nth]:
            nth = index
        mode = chr(nth + ord('a'))

    return mode


result = find_max_occurred_alphabet(input)
print(result)