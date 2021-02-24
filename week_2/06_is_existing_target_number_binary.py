finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


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


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)