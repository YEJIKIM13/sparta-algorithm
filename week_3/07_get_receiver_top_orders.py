top_heights = [6, 9, 5, 7, 4]


# 레이저 방향이 왼쪽이니까, 왼쪽이랑 비교겠구나 하고 생각!
# 자신보다 왼쪽에 있는 탑들을 하나하나 비교하면서 처음 자기보다 같거나(같거나는 X, 문제에 명시) 큰 원소 찾으면 됨!
def get_receiver_top_orders(heights):
    top_array = []
    for i in range(len(heights)):  # 0, 1, ..., len(heights)-1
        # i 는 그 요소 위치용, j 는 비교 시 인덱스 줄여주기 위한 용도
        for j in range(i + 1):
            if heights[i] < heights[i - j]:
                top_array.append(i - j + 1)  # 몇 번째 '기둥' 인지가 기록되어야 하니까
                break
        # for 문 다 돌았는데도 없다면 0 추가
        else:
            top_array.append(0)

    return top_array


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
