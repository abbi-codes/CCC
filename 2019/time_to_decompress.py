lines = int(input())
instructions = [input().split() for i in range(lines)]
output = []

for given in instructions:
    output.append(int(given[0]) * given[1])

for out in output:
    print(out)