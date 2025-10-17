given_str = input()
sub_str = input()
len_sub = len(sub_str) - 1
all_poss = [sub_str]
current_sub = sub_str
output = "no"

for i in range(len_sub):
    sub = current_sub[0]
    current_sub = current_sub[1:] + sub
    # current_sub += sub
    all_poss.append(current_sub)

for poss in all_poss:
    if poss in given_str:
        output = "yes"
        break

print(output)