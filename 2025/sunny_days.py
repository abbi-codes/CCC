n = int(input())
m = 0
all_data = []

def find_max(data):
    most_max = 0
    my_curr_max = 0
    for a in range(n):
        if data[a] == 1:
            my_curr_max += 1
        elif data[a] == 0:
            my_curr_max = 0
        if my_curr_max >= most_max:
            most_max = my_curr_max
    return most_max

for i in range(n):
    sun_or_prec = input()
    if sun_or_prec == "S":
        all_data.append(1)
    else:
        all_data.append(0)

for j in range(n):
    if all_data[j] == 0:
        all_data[j] = 1
        curr_max = find_max(all_data)
        all_data[j] = 0
    else:
        all_data[j] = 0
        curr_max = find_max(all_data)
        all_data[j] = 1
    if curr_max > m:
        m = curr_max
    curr_max = 0

print(m)










