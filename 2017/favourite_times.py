duration = int(input())
total_seq_one_day = 0
total_seq_of_remainder = 0
half_days = duration // (12 * 60)
remainder = duration % (12 * 60)
curr_mins = 0

def is_arithmetic(given_hour, given_min):
    my_list = []
    if given_hour > 9:
        my_list.append(1)
    my_list.append(given_hour % 10)

    if given_min > 9:
        my_list.append(given_min // 10)
    else:
        my_list.append(0)
    my_list.append(given_min % 10)

    if len(my_list) == 3:
        if (my_list[1] - my_list[0]) == (my_list[2] - my_list[1]):
            return True
    else:
        if (my_list[1] - my_list[0]) == (my_list[2] - my_list[1]) == (my_list[3] - my_list[2]):
            return True
    return False

for hour in range(0, 12):
    if hour == 0:
        real_hour = 12
    else:
        real_hour = hour
    for minute in range(60):
        if is_arithmetic(real_hour, minute):
            total_seq_one_day += 1
            if curr_mins <= remainder:
                total_seq_of_remainder += 1
        curr_mins += 1

print(half_days * total_seq_one_day + total_seq_of_remainder)