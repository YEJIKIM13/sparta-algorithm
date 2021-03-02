input = [4, 6, 2, 9, 1]


# 정렬할 개수, 봐야하는 것, 내부적 구현!
def selection_sort(array):
    # 가장 작은 수부터 인덱스에 넣어야 하니까
    for i in range(len(array) - 1):  # 하나 나은 원소를 비교하지 않으니 1 뺀다
        min_index = i  # 비교 가준의 처음 인덱스
        for j in range(len(array) - i):
            if array[i + j] < array[min_index]:  # 현재 시도해보고 있는 인덱스, 더해줌으로써 올려치기!!
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]  # 지금 i 번째 자리 정하고 있는 거니까

    return array


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
