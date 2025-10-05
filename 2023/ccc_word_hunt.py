word = input()
rev_word = []

for char in word:
    rev_word.insert(0, char)

str_rev_word = ""

for char in rev_word:
    str_rev_word += char

rows = int(input())
cols = int(input())
grid = []
total = 0

for i in range(rows):
    grid.append(list(map(str, input().split())))

new_grid = []
for j in grid:
    string = ""
    for letter in j:
        string += letter
    new_grid.append(string)

for r in new_grid:
    if word in r:
        total += 1
    elif str_rev_word in r:
        total += 1

print(total)