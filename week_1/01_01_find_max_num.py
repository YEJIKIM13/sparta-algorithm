input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 배열의 숫자 하나하나 꺼내야 되니까 반복문 사용
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)