keys_pressed = input()
displayed = input()

ordered_keys_pressed_no_repeat = []
ordered_keys_displayed_no_repeat = []

prev_key = ""
for let in keys_pressed:
    if let != prev_key:
        ordered_keys_pressed_no_repeat.append(let)
        prev_key = let
len_keys_pressed = len(ordered_keys_pressed_no_repeat)

prev_key = ""
for lett in displayed:
    if lett != prev_key:
        ordered_keys_displayed_no_repeat.append(lett)
        prev_key = lett
len_displayed = len(ordered_keys_displayed_no_repeat)

diff_keys_pressed = set(keys_pressed)
diff_keys_displayed = set(displayed)
silly_key = "" 
corres_silly_key = ""
quiet_key = ""
quiet_silly = []

for chrc in diff_keys_displayed:
    if chrc not in diff_keys_pressed:
        silly_key = chrc
        break

for my_key in diff_keys_pressed:
    if my_key not in diff_keys_displayed:
        quiet_silly.append(my_key)

if len(quiet_silly) == 1:
    corres_silly_key = quiet_silly[0]
    for i in range(len_displayed):
        if keys_pressed[i] != displayed[i]:
            silly_key = displayed[i]
else:
    for i in range(len_displayed):
        if ordered_keys_displayed_no_repeat[i] != ordered_keys_pressed_no_repeat[i]:
            if ordered_keys_pressed_no_repeat[i + 1] != ordered_keys_displayed_no_repeat[i]:
                corres_silly_key = ordered_keys_pressed_no_repeat[i]
                if quiet_silly[0] == corres_silly_key:
                    quiet_key = quiet_silly[1]
                else:
                    quiet_key = quiet_silly[0]
                break
            else:
                quiet_key = ordered_keys_pressed_no_repeat[i]
                if quiet_silly[0] == quiet_key:
                    corres_silly_key = quiet_silly[1]
                else:
                    corres_silly_key = quiet_silly[0]
                break

if silly_key == "":
    for i in range(len_displayed):
        if keys_pressed[i] != displayed[i]:
            silly_key = displayed[i]

print(corres_silly_key, silly_key)

if quiet_key == "":
    print('-')
else:
    print(quiet_key)