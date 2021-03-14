seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo  # fibo_memo 에 기록하기
    return nth_fibo  # 기록 후 반환하기


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    count = 1
    curr_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        curr_count = fibo_dynamic_programming(fixed_seat_index - curr_index, memo)
        count *= curr_count
        curr_index = fixed_seat_index + 1

    curr_count = fibo_dynamic_programming(total_count - curr_index, memo)
    count *= curr_count

    return count


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
