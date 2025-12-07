n = int(input())
k = int(input())
shifty_num = n

for i in range(1, k + 1):
    shifty_num += n * (10 ** i)

print(shifty_num)