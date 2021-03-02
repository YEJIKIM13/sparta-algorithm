array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    result_array = []
    # array1과 array2를 인덱스를 하나하나 잡아서 얘네들을 비교하면서 더 작은 애 넣어주곤 했음
    array1_index = 0  # 인덱스를 저장할 변수, 포인터
    array2_index = 0  # 인덱스를 저장할 변수, 포인터
    # 언제까지 반복?
    while array1_index < len(array1) and array2_index < len(array2):
        # 비교하기
        if array1[array1_index] < array2[array2_index]:
            # result_array 에 더 작은 값 추가하기
            result_array.append(array1[array1_index])
            array1_index += 1
        else:
            result_array.append(array2[array2_index])
            array2_index += 1

    # 남는 거 넣어주기
    # 만약 array1이 끝나고 array2가 남아있다면
    if array1_index == len(array1):
        while array2_index < len(array2):
            result_array.append(array2[array2_index])
            array2_index += 1

    # 만약 array2가 끝나고 array1이 남아있다면
    if array2_index == len(array2):
        while array1_index < len(array1):
            result_array.append(array1[array1_index])
            array1_index += 1

    return result_array


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
