input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count = 0
    for index in range(len(string)-1):
        if string[index] != string[index +1]:
            count += 1
    return (count + 1)  //  2


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
