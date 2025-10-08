side_len = int(input())
num_trees = int(input())
row_col = list(map(int, input().split()))

print(side_len - min(row_col[0], row_col[1], side_len - row_col[0] + 1, side_len - row_col[1] + 1))