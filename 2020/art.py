num_drops = int(input())
bottom_left = [100, 100]
top_right = [0, 0]

for i in range(num_drops):
    x, y = list(map(int, input().split(",")))

    if x < bottom_left[0]:
        bottom_left[0] = x
    if x > top_right[0]:
        top_right[0] = x
    if y < bottom_left[1]:
        bottom_left[1] = y
    if y > top_right[1]:
        top_right[1] = y

print(f"{bottom_left[0] - 1}, {bottom_left[1] - 1}")
print(f"{top_right[0] + 1}, {top_right[1] + 1}")