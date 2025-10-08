side_len = int(input())
num_trees = int(input())
all_trees = []
max_len = 0
for i in range(num_trees):
    all_trees.append(list(map(int, input().split())))

def largest_pool(start_point, length):
    in_grid = []
    all_max = []
    row, col = start_point[0] + length, start_point[1] + length
    for point in all_trees:
        x, y = point
        if start_point[0] <= x <= row and start_point[1] <= y <= col:
            in_grid.append([x, y])
    if in_grid == []:
        return length
    for tree in in_grid:
        all_max.append(max(tree[0] - start_point[0], tree[1] - start_point[1]))
    return min(all_max)

for a in range(1, side_len + 1):
    for b in range(1, side_len + 1):
        top_left = [a, b]
        curr_len = min(side_len - a + 1, side_len - b + 1)
        pool_size = largest_pool(top_left, curr_len)
        if pool_size > max_len:
            max_len = pool_size

print(max_len)