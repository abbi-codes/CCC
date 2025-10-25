my_last_digits = []

for i in range(4):
    my_last_digits.append(int(input()))

if (my_last_digits[0] == 8 or my_last_digits[0] == 9) and (my_last_digits[3] == 8 or my_last_digits[3] == 9) and (my_last_digits[1] == my_last_digits[2]):
    print("ignore")
else:
    print("answer")