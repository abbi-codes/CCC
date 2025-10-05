num_cols = int(input())
all = []
prev_f = 0
prev_s = 0
total_points = 0

for i in range(2):
    all.append(list(map(int, input().split())))

for i in range(num_cols):
    first = all[0][i]
    second = all[1][i]
    total_points += first * 3 + second * 3
    if first == second == 1:
        total_points -= 2
    if prev_f == first == 1:
        total_points -= 2
    if prev_s == second == 1:
        total_points -= 2
    prev_f = first
    prev_s = second

print(total_points)