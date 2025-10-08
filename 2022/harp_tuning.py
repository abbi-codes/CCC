instructions = input()
previous_is_num = False
strings = "ABCDEFGHIJKLMNOPQRST"
output = []
sub_out = ""

for charac in instructions:
    if charac in strings:
        if previous_is_num:
            output.append(sub_out)
            previous_is_num = False
            sub_out = charac
        else:
            sub_out += charac
    elif charac == "+":
        sub_out += " tighten "
    elif charac == "-":
        sub_out += " loosen "
    else:
        sub_out += charac
        previous_is_num = True

output.append(sub_out)

for line in output:
    print(line)