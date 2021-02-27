shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()  # 정렬의 시간복잡도는 보통 배열의 길이를 N 이라고 한다면 O(N * logN)
    for menu_order in orders:
        # 없다면 즉시 False 리턴하고 함수 종료
        # 이분 탐색 호출하는 시간 O(logN) 인데 그걸 orders 의 길이만큼 반복, 결국 O(M * logN)
        if not is_existing_target_number_binary(menu_order, menus):  # not (없다(False)) == True -> 없을 때 조건이 참이 되며 실행이 됨
            return False
    return True
    # O((M+N) * logN)

# 이진 탐색 함수 가져다 쓰기
def is_existing_target_number_binary(target, array):
    start = 0  # current_min
    end = len(array) - 1  # current_max
    curr = (start + end) // 2  # current_guess

    # 조건은 어떻게 세울래? -> 같지 않을 동안 반복 or 작은 경우, 큰 경우
    # 로직은 범위 값들을 바꿔주면 될 듯. ((범위의)최솟값, 시돗값, (범위의)최댓값)
    # 조건 설정이 미숙해...
    while start <= end:
        if array[curr] == target:
            return True  # 값 찾으면 함수 리턴하며 종료
        elif array[curr] > target:
            end = curr - 1  # 최댓값 낮추기 (다운)
        else:
            start = curr + 1  # 최솟값 높이기 (업)
        curr = (start + end) // 2  # 업데이트 해야함
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
