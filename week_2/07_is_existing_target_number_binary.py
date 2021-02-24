finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    # 이 부분을 채워보세요!
    # 정렬해야 이진탐색 가능
    sort_numbers = numbers.sort()

    return 1


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)