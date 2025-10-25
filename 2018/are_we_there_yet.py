import math

my_input = list(map(int, input().split()))
my_input.insert(0, 0)
current = 0
coord = []

for dist in my_input:
    current = current + dist
    coord.append(current)

for i in range(5):
    line = ""
    my_distance = 0
    for j in range(5):
        line += str(abs(coord[i] - coord[j]))
        line += " "
    line = line.strip()
    print(line) 