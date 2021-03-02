input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    for i in range(1, len(array)):  # 혼자 있는 0 번째 인덱스는 정렬된 상태라고 치고 들어가기
        for j in range(i):  # 해당하는 인덱스까지 비교 (i 가 늘어날 때마다 j 내부에 있는 반복의 횟수가 똑같이 증가되기 때문에)
            # 현재 시도해보고 있는 인덱스는 i - j (인덱스가 4, 3, 2, 1) 이렇게 나옴
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!
