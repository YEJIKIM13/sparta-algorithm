input = [4, 6, 2, 9, 1]

# [4, 6, 2, 9, 1]
#   -> -> -> ->
# [4, 2, 6, 1, 9]
#   -> -> ->
# [2, 4, 1, 6, 9]
#   -> ->
# [2, 1, 4, 6, 9]
#   ->
# [1, 2, 4, 6, 9]


def bubble_sort(array):
    # 근데 이걸 뒤에서부터 하나씩 줄여가면서 반복해야 하는데... -> 반복되는 구조라 반복문 사용
    # ~ 번째 반복 부분
    for i in range(len(array) - 1):  # n의 길이
        # 한 칸씩 이동하면서 비교하기
        for j in range(len(array) - 1 - i):  # 비교하는 과정, len(array)-1 번 비교에서 i 번째만큼 덜 비교, 하나씩 줄어들면서 덜 비교, n의 길이
            # 좌, 우 비교해서 대소에 따라 바꿔주기
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        # 근데 이걸 뒤에서부터 하나씩 줄여가면서 반복해야 하는데...

    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
