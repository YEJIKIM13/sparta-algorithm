numbers = [1, 1, 1, 1, 1]  # 참고 -> 만약에 2, 3, 4 면 어떻게 해야 3이라는 값을 구할 수 있는지, 없는지에 대해 고민하고 사고 확장...
target_number = 3
count = 0


# 배열, 타겟넘버, 현재 인덱스, 현재 해당하는 합계
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, curr_index, curr_sum):
    if curr_index == len(numbers):
        if curr_sum == target:
            global count
            count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, curr_index + 1, curr_sum + numbers[curr_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, curr_index + 1, curr_sum - numbers[curr_index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
print(count)  # 5를 반환해야 합니다!
